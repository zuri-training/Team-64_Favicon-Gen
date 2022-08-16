from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import SignUpForm, SignInForm, ForgottenPasswordForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail

import time
import os
import zipfile
import shutil
# import pyvips
# import cairosvg
from PIL import Image
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
# ************************

# START:for_download_tuto
from .models import FilesAdmin, FaviconZipFile, GeneratedFavicon, UploadedFile, ConvertedFavicon, Texticons, UserTexticon
from django.urls import reverse
from django.core.files.base import ContentFile, File
# END:for_download_tuto
# Create your views here.

def mail(request):
    subject = 'your subject'
    message = 'your message'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["receiver's mail address", ]
    # return render(request,'login.html')
    return redirect('/sign-in')

def home(request):
    return render(request, 'pages/home.html')

def reviews(request):
    return render(request, 'pages/reviews.html')

def tutorial(request):
    return render(request, 'pages/tutorial.html')

def texticons(request):
    texticonsList = Texticons.objects.all()
    if request.user.id :
        userSavedTexticonsList= UserTexticon.objects.filter(user = request.user)
        context={"texticonsList": []}
        
        for texticonItem in texticonsList:
            savedItem = False
            for userSavedTexticon in userSavedTexticonsList:
                if texticonItem.id == userSavedTexticon.texticon.id :
                    savedItem = True
                    context["texticonsList"].append({"texticonItem": texticonItem, "savedToDrafts": 1})
                    break
            
            if savedItem == False :
                context["texticonsList"].append({"texticonItem": texticonItem, "savedToDrafts": 0})

        return render(request, 'pages/texticons.html', context)
    else:
        context={"texticonsList": []}
        for texticonItem in texticonsList:
            context["texticonsList"].append({"texticonItem": texticonItem, "savedToDrafts": 0})            

        return render(request, 'pages/texticons.html', context)

@login_required(login_url="/sign-in")
def saveTexticonToDrafts(request):
    if request.method == 'POST':
        current_user = request.user
        texticonId = request.POST['texticon_id'] 
        texticon = Texticons.objects.get(id=texticonId)
        user_texticon = UserTexticon(
            user=current_user,
            texticon= texticon,
            saved_to_drafts = True
        )
        user_texticon.save()
        return JsonResponse({'texticonId' : texticonId})












def generatorPage(request):
    return render(request, 'pages/generator.html')

@login_required(login_url="/sign-in")
def faviconGeneration(request, document_root):
    if request.method == 'POST':
        current_user = request.user
        timestr = time.strftime("%Y%m%d-%H%M%S")
        mainName = 'ZuriconGen-'+current_user.username+'-'+timestr
        genFileName = 'ZuriconGen_Favicon_Generation'
        pathToGeneratedFiles = os.path.join(document_root,'generator', mainName)
        relativePathToGeneratedFiles = os.path.join('generator', mainName)
        html_codes = []
        savedToDrafts = False
        try:
            svgContent = request.POST['sgenerator_svg_content']
            savedToDrafts = request.POST['saved_to_drafts']     
            os.mkdir(pathToGeneratedFiles)
            # CREATE ZIP FILE
            my_zip = zipfile.ZipFile(os.path.join(pathToGeneratedFiles,mainName+'.zip'), 'w')
            # SAVE ZIP FILE IN THE DATABASE
            gen_zipfile = FaviconZipFile(user=current_user, name=mainName, saved_to_drafts=savedToDrafts)            
            gen_zipfile.path.name=os.path.join(relativePathToGeneratedFiles,mainName+'.zip')
            gen_zipfile.save()

            # CREATE SVG FILE
            fsvg = open(os.path.join(pathToGeneratedFiles,genFileName+".svg"), "w")
            fsvg.write(svgContent)
            fsvg.close()
            # SAVE SVG FILE IN THE DATABASE
            gen_favicon_svg = GeneratedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=genFileName,                
                img_type="svg",
                size=120,
                saved_to_drafts=savedToDrafts,
                html_code="<link rel='icon' sizes='120x120' href='"+genFileName+".svg'>"
            )            
            gen_favicon_svg.path.name=os.path.join(relativePathToGeneratedFiles,genFileName+'.svg')
            gen_favicon_svg.save()
            
            html_codes.append("<link rel='icon' href='"+genFileName+".svg'>\n")
            my_zip.write(pathToGeneratedFiles+"/"+genFileName+".svg", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""), genFileName+".svg"))
            
            # Copy svg file
            shutil.copy(
                os.path.join(pathToGeneratedFiles,genFileName+".svg"), 
                os.path.join(pathToGeneratedFiles,genFileName+"-Copy.svg")
            )
            lines = []
            copyPath = os.path.join(pathToGeneratedFiles,genFileName+"-Copy.svg")
            # read file
            with open(copyPath, 'r') as fp:
                lines = fp.readlines()
            # Write file : remove line 8            
            with open(copyPath, 'w') as fp:
                for number, line in enumerate(lines):
                    if number not in [4]:
                        fp.write(line)
                
            drawing = svg2rlg(copyPath)
            renderPM.drawToFile(drawing, os.path.join(pathToGeneratedFiles,genFileName+".png"), fmt="PNG")            

            pathToImgToConvert = os.path.join(pathToGeneratedFiles,genFileName+".png")
            
            # generate Favicon Files
            formatsList = ["png", "jpg", "ico"]
            sizesList = [16, 32, 96, 180]
            for imgFormat in formatsList:
                for size in sizesList:
                    generateFaviconFile("generation", savedToDrafts, current_user, gen_zipfile, pathToGeneratedFiles, relativePathToGeneratedFiles, 
                            pathToImgToConvert, genFileName, imgFormat, size)
                    
                    code = "<link rel='icon' sizes='"+str(size)+"x"+str(size)+"' href='"+genFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat+"'>\n"
                    html_codes.append(code)

                    my_zip.write(pathToGeneratedFiles+"/"+genFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat, arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""), genFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat))

            ftxt = open(pathToGeneratedFiles+"/html_codes.txt", "a")            
            for code in html_codes:
                ftxt.write(code)            
            ftxt.close()
            my_zip.write(pathToGeneratedFiles+"/html_codes.txt", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""),"html_codes.txt"))
            my_zip.close()
            # end
            os.remove(copyPath)
            os.remove(os.path.join(pathToGeneratedFiles,genFileName+".png"))
        
            zip_toDownload = open(os.path.join(pathToGeneratedFiles,mainName+'.zip'), 'rb')
            response = FileResponse(zip_toDownload)             
            return response

        except KeyError:
            print ('Where is my svg content ?')
            return redirect('error_w')


















def converterPage(request):
    return render(request, 'pages/converter.html')

@login_required(login_url="/sign-in")
def faviconConversion(request, document_root):
    if request.method == 'POST':
        current_user = request.user
        timestr = time.strftime("%Y%m%d-%H%M%S")
        mainName = 'ZuriconGen-'+ current_user.username+'-'+timestr
        convFileName = 'ZuriconGen_Favicon_Conversion'
        html_codes = []
        savedToDrafts = False
        try:
            # imgToConvert = request.FILES['imgToConvert']
            imgToConvert = request.FILES['uploadedImg']
            savedToDrafts = request.POST['saved_to_drafts']  
            uploadedImgObj = UploadedFile(name=mainName, path=imgToConvert, user=current_user)
            uploadedImgObj.save()
            
            pathToUploadedImg = os.path.join(document_root, uploadedImgObj.path.name)
            pathToConvertedFiles = os.path.join(document_root,'converter', mainName)
            relativePathToConvertedFiles = os.path.join('converter', mainName)
            # relativePathToConvertedFiles = pathToConvertedFiles

            os.mkdir(pathToConvertedFiles)
            # CREATE ZIP FILE
            my_zip = zipfile.ZipFile(os.path.join(pathToConvertedFiles,mainName+'.zip'), 'w')
            # SAVE ZIP FILE IN THE DATABASE
            gen_zipfile = FaviconZipFile(user=current_user, name=mainName, saved_to_drafts=savedToDrafts)            
            gen_zipfile.path.name=os.path.join(relativePathToConvertedFiles,mainName+'.zip')
            gen_zipfile.save()            
            

            formatsList = ["png", "jpg", "ico"]
            sizesList = [16, 32, 96, 180]
            for imgFormat in formatsList:
                for size in sizesList:
                    generateFaviconFile("conversion",  savedToDrafts, current_user, gen_zipfile, pathToConvertedFiles, relativePathToConvertedFiles, 
                            pathToUploadedImg, convFileName, imgFormat, size)
                    
                    code = "<link rel='icon' sizes='"+str(size)+"x"+str(size)+"' href='"+convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat+"'>\n"
                    html_codes.append(code)

                    my_zip.write(pathToConvertedFiles+"/"+convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat, arcname=os.path.join(pathToConvertedFiles.replace(pathToConvertedFiles, ""), convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat))

            ftxt = open(pathToConvertedFiles+"/html_codes.txt", "a")            
            for code in html_codes:
                ftxt.write(code)            
            ftxt.close()
            my_zip.write(pathToConvertedFiles+"/html_codes.txt", arcname=os.path.join(pathToConvertedFiles.replace(pathToConvertedFiles, ""),"html_codes.txt"))
            my_zip.close()
            # Delete uploaded file
            uploadedImgObj.delete()  

            zip_toDownload = open(os.path.join(pathToConvertedFiles,mainName+'.zip'), 'rb')
            response = FileResponse(zip_toDownload, mainName+'.zip')             
            return response

        except KeyError:
            return redirect('error_w')






def createTexticons(request):
    if request.method == 'POST':
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        mainName = 'ZuriconGen_Texticon_'
        
        try:
            for letter in letters:
                relativePathToTexticonImage = os.path.join('texticons', 'images', mainName+letter+'.svg')
                relativePathToTexticonZipFile = os.path.join('texticons', 'zipfiles', mainName+letter+'.zip')
                texticonObj = Texticons(
                    name=mainName+letter,                
                    img_type="svg",
                    html_code="<link rel='icon' href='"+mainName+letter+".svg'>"
                )            
                texticonObj.img_path.name=relativePathToTexticonImage
                texticonObj.zip_path.name=relativePathToTexticonZipFile
                texticonObj.save()
            
            return HttpResponse('Texticons created successfully !')

        except KeyError:
            return redirect('error_w')
    
    return render(request, 'main/createTexticons.html')



def drafts(request, document_root):
    downloadedGenfavicons = GeneratedFavicon.objects.filter(user = request.user, img_type="svg", saved_to_drafts = False).order_by("-id")
    downloadedConvfavicons = ConvertedFavicon.objects.filter(user = request.user, img_type="png", size=96, saved_to_drafts = False).order_by("-id")
    savedGenfavicons = GeneratedFavicon.objects.filter(user = request.user, img_type="svg", saved_to_drafts = True).order_by("-id")
    savedConvfavicons = ConvertedFavicon.objects.filter(user = request.user, img_type="png", size=96, saved_to_drafts = True).order_by("-id")
    userSavedTexticonsList= UserTexticon.objects.filter(user = request.user)
    context={"savedGenfavicons": [], "savedConvfavicons": [], "savedTexticons": [], "downloadedGenfavicons": [], "downloadedConvfavicons": []}
    for fav in downloadedGenfavicons:
        zipId = fav.zip_file.id
        ziplink = FaviconZipFile.objects.get(id=zipId)
        context["downloadedGenfavicons"].append({"favicon": fav, "ziplink":ziplink})
    
    for fav in downloadedConvfavicons:
        zipId = fav.zip_file.id
        ziplink = FaviconZipFile.objects.get(id=zipId)
        context["downloadedConvfavicons"].append({"favicon": fav, "ziplink":ziplink})

    for fav in savedGenfavicons:
        zipId = fav.zip_file.id
        ziplink = FaviconZipFile.objects.get(id=zipId)
        context["savedGenfavicons"].append({"favicon": fav, "ziplink":ziplink})
    
    for fav in savedConvfavicons:
        zipId = fav.zip_file.id
        ziplink = FaviconZipFile.objects.get(id=zipId)
        context["savedConvfavicons"].append({"favicon": fav, "ziplink":ziplink})

    for userSavedTexticon in userSavedTexticonsList:
        texticon = Texticons.objects.get(id = userSavedTexticon.texticon.id)
        context["savedTexticons"].append({"texticon": texticon})

    return render(request, 'pages/drafts.html', context)







def deleteFavicon(request, value):
    zipId = value
    try:
        faviconsToDelete = []
        faviconsToDelete = GeneratedFavicon.objects.filter(user = request.user, zip_file_id=zipId)
        if len(faviconsToDelete) == 0:
            faviconsToDelete = ConvertedFavicon.objects.filter(user = request.user, zip_file_id=zipId)

        for fav in faviconsToDelete:
            fav.delete()
        
        zipFileToDelete = FaviconZipFile.objects.get(id=zipId)
        zipFileToDelete.delete()
        
        return redirect('drafts')

    except KeyError:
            return redirect('error_w')

def deleteSavedTexticon(request, value):
    texticonId = value
    try:        
        userSavedTexticonToDelete= UserTexticon.objects.get(texticon_id = texticonId)
        userSavedTexticonToDelete.delete()
        return redirect('drafts')
    except KeyError:
        return redirect('error_w')






# START AUTHENTICATION
def sign_in(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
    else:
        return redirect('/home')

    form = SignInForm()
    return render(request, 'auth/signin.html', {"form":form})

def sign_up(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                print("FORM IS VALID - FORM IS VALID - FORM IS VALID")
                username =form.cleaned_data.get("username")
                password =form.cleaned_data.get("password1")
                form.save()
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login(request, new_user)
                    return redirect('/home')
    else:
        return redirect('/home')
    
    form = SignUpForm()
    return render(request, 'auth/signup.html', {"form":form})

# def forgotten_password(request):
#     form = ForgottenPasswordForm()
#     return render(request, 'auth/forgotten_password_form.html', {"form":form})

# END AUTHENTICATION


# ************************
def success(request, filelink):
    return render(request, 'main/success.html', {"filelink":filelink})

def error_w(request):
	return HttpResponse('There was an error !')
# ************************


# START EXTRA FUNCTIONS 
def generateFaviconFile(convGen, savedToDrafts, current_user, gen_zipfile, pathToFiles, relativePathToFiles, 
                            pathToImgToConvert, convFileName, imgFormat, size):

    img = Image.open(pathToImgToConvert)
    if (imgFormat == "jpg"):
        img = img.convert('RGB')
    
    if (imgFormat == "ico"):
        img.save(os.path.join(pathToFiles,convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat), format='ICO', sizes=[(size,size)])
    else:
        img.thumbnail((size, size))
        img.save(os.path.join(pathToFiles,convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat))

    if (convGen == "generation"):
        convgen_favicon = GeneratedFavicon(
            user=current_user,
            zip_file=gen_zipfile,
            name=convFileName,                
            img_type=imgFormat,
            size=size,
            saved_to_drafts=savedToDrafts,
            html_code="<link rel='icon' sizes='"+str(size)+"x"+str(size)+"' href='"+convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat+"'>"
        ) 
    elif (convGen == "conversion"):
        convgen_favicon = ConvertedFavicon(
            user=current_user,
            zip_file=gen_zipfile,
            name=convFileName,                
            img_type=imgFormat,
            size=size,
            saved_to_drafts=savedToDrafts,
            html_code="<link rel='icon' sizes='"+str(size)+"x"+str(size)+"' href='"+convFileName+"-"+str(size)+"x"+str(size)+"."+imgFormat+"'>"
        )            
    convgen_favicon.path.name=os.path.join(relativePathToFiles,convFileName+'-'+str(size)+'x'+str(size)+'.'+imgFormat)
    convgen_favicon.save()

# END EXTRA FUNCTIONS 