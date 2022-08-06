from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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
from .models import FilesAdmin, FaviconZipFile, GeneratedFavicon, UploadedFile, ConvertedFavicon
from django.urls import reverse
from django.core.files.base import ContentFile, File
# END:for_download_tuto
# Create your views here.

@login_required(login_url="/login")
def home(request):
    # START:for_download_tuto
    context = {'file':FilesAdmin.objects.all()}
    return render(request, 'main/home.html', context)
    # END:for_download_tuto


@login_required(login_url="/login")
def generatorPage(request, document_root):
    if request.method == 'POST':
        current_user = request.user
        try:
            svgContent = request.POST['sgenerator_svg_content']
            
            timestr = time.strftime("%Y%m%d-%H%M%S")
            mainName = 'ZuriconGen-'+current_user.username+'-'+timestr
            genFileName = 'ZuriconGen_Favicon_Generation'
            pathToGeneratedFiles = os.path.join(document_root,'generator', mainName)
            relativePathToGeneratedFiles = os.path.join('generator', mainName)
            # relativePathToGeneratedFiles = pathToGeneratedFiles

            os.mkdir(pathToGeneratedFiles)
            # CREATE ZIP FILE
            my_zip = zipfile.ZipFile(os.path.join(pathToGeneratedFiles,mainName+'.zip'), 'w')
            # SAVE ZIP FILE IN THE DATABASE
            gen_zipfile = FaviconZipFile(user=current_user, name=mainName)            
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
                html_code="<link rel='icon' sizes='120x120' href='"+genFileName+".svg'>"
            )            
            gen_favicon_svg.path.name=os.path.join(relativePathToGeneratedFiles,genFileName+'.svg')
            gen_favicon_svg.save()
            
            # CREATE PNG FILE
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
                    if number not in [8]:
                        fp.write(line)
                
            drawing = svg2rlg(copyPath)
            renderPM.drawToFile(drawing, os.path.join(pathToGeneratedFiles,genFileName+".png"), fmt="PNG")            
            imgPNG = Image.open(os.path.join(pathToGeneratedFiles,genFileName+".png"))
            imgPNG.thumbnail((64, 64))
            imgPNG.save(os.path.join(pathToGeneratedFiles,genFileName+"-64x64.png"))

            os.remove(copyPath)
            os.remove(os.path.join(pathToGeneratedFiles,genFileName+".png"))

            gen_favicon_png = GeneratedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=genFileName,                
                img_type="png",
                html_code="<link rel='icon' sizes='64x64' href='"+genFileName+"-64x64.png'>"
            )            
            gen_favicon_png.path.name=os.path.join(relativePathToGeneratedFiles,genFileName+'-64x64.png')
            gen_favicon_png.save()

            # CREATE JPG FILE
            imgJPG = Image.open(os.path.join(pathToGeneratedFiles,genFileName+"-64x64.png"))
            imgJPG.save(os.path.join(pathToGeneratedFiles,genFileName+"-64x64.jpg"))
            # SAVE JPG FILE IN THE DATABASE
            gen_favicon_jpg = GeneratedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=genFileName,                
                img_type="jpg",
                html_code="<link rel='icon' sizes='64x64' href='"+genFileName+"-64x64.jpg'>"
            )            
            gen_favicon_jpg.path.name=os.path.join(relativePathToGeneratedFiles,genFileName+'-64x64.jpg')
            gen_favicon_jpg.save()

            # CREATE ICO FILE
            img = Image.open(os.path.join(pathToGeneratedFiles,genFileName+"-64x64.png"))
            img.save(os.path.join(pathToGeneratedFiles,genFileName+"-32x32.ico"), format='ICO', sizes=[(32,32)])
            # SAVE ICO FILE IN THE DATABASE
            gen_favicon_ico = GeneratedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=genFileName,                
                img_type="ico",
                html_code="<link rel='icon' sizes='64x64' href='"+genFileName+"-32x32.ico'>"
            )            
            gen_favicon_ico.path.name=os.path.join(relativePathToGeneratedFiles,genFileName+'-32x32.ico')
            gen_favicon_ico.save()
            
            
            # CREATE HTML_CODE.TXT FILE
            html_codes = [
                
                "<link rel='icon' sizes='120x120' href='"+genFileName+".svg'>\n",
                "<link rel='icon' sizes='64x64' href='"+genFileName+"-64x64.png'>\n",
                "<link rel='icon' sizes='64x64' href='"+genFileName+"-64x64.jpg'>\n",
                "<link rel='icon' sizes='32x32' href='"+genFileName+"-32x32.ico'>\n",
            ]
            ftxt = open(pathToGeneratedFiles+"/html_codes.txt", "a")            
            for code in html_codes:
                ftxt.write(code)            
            ftxt.close()


            # my_zip = zipfile.ZipFile(pathToGeneratedFiles+"/"+genFileName+'.zip', 'w')
            my_zip.write(pathToGeneratedFiles+"/"+genFileName+".svg", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""), genFileName+".svg"))
            my_zip.write(pathToGeneratedFiles+"/"+genFileName+"-64x64.png", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""), genFileName+"-64x64.png"))
            my_zip.write(pathToGeneratedFiles+"/"+genFileName+"-64x64.jpg", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""), genFileName+"-64x64.jpg"))
            my_zip.write(pathToGeneratedFiles+"/"+genFileName+"-32x32.ico", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""), genFileName+"-32x32.ico"))
            my_zip.write(pathToGeneratedFiles+"/html_codes.txt", arcname=os.path.join(pathToGeneratedFiles.replace(pathToGeneratedFiles, ""),"html_codes.txt"))
            my_zip.close()
        

            zip_toDownload = open(os.path.join(pathToGeneratedFiles,mainName+'.zip'), 'rb')
            response = FileResponse(zip_toDownload)             
            return response

            # return render(request, 'main/success.html', {"filelink":gen_zipfile.path, 
            #                                             "statusMessage":"Successfully generated favicon!",
            #                                             "goBack":"/generator_page"})

        except KeyError:
            print ('Where is my svg content ?')
            return redirect('error_w')

    return render(request, 'generator_page/generator.html')
















# @login_required(login_url="/login")
def converterPage(request, document_root):
    if request.method == 'POST':
        current_user = request.user
        timestr = time.strftime("%Y%m%d-%H%M%S")
        mainName = 'ZuriconGen-'+ current_user.username+'-'+timestr
        convFileName = 'ZuriconGen_Favicon_Conversion'
        try:
            # imgToConvert = request.FILES['imgToConvert']
            imgToConvert = request.FILES['uploadedImg']

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
            gen_zipfile = FaviconZipFile(user=current_user, name=mainName)            
            gen_zipfile.path.name=os.path.join(relativePathToConvertedFiles,mainName+'.zip')
            gen_zipfile.save()            
            
            # CREATE PNG FILE            
            imgPNG = Image.open(pathToUploadedImg)
            imgPNG.thumbnail((64, 64))
            imgPNG.save(os.path.join(pathToConvertedFiles,convFileName+"-64x64.png"))

            gen_favicon_png = ConvertedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=convFileName,                
                img_type="png",
                html_code="<link rel='icon' sizes='64x64' href='"+convFileName+"-64x64.png'>"
            )            
            gen_favicon_png.path.name=os.path.join(relativePathToConvertedFiles,convFileName+'-64x64.png')
            gen_favicon_png.save()

            # CREATE JPG FILE
            imgJPG = Image.open(os.path.join(pathToConvertedFiles,convFileName+"-64x64.png"))
            imgJPG.save(os.path.join(pathToConvertedFiles,convFileName+"-64x64.jpg"))
            # SAVE JPG FILE IN THE DATABASE
            gen_favicon_jpg = ConvertedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=convFileName,                
                img_type="jpg",
                html_code="<link rel='icon' sizes='64x64' href='"+convFileName+"-64x64.jpg'>"
            )            
            gen_favicon_jpg.path.name=os.path.join(relativePathToConvertedFiles,convFileName+'-64x64.jpg')
            gen_favicon_jpg.save()

            # CREATE ICO FILE
            img = Image.open(os.path.join(pathToConvertedFiles,convFileName+"-64x64.png"))
            img.save(os.path.join(pathToConvertedFiles,convFileName+"-32x32.ico"), format='ICO', sizes=[(32,32)])
            # SAVE ICO FILE IN THE DATABASE
            gen_favicon_ico = ConvertedFavicon(
                user=current_user,
                zip_file=gen_zipfile,
                name=convFileName,                
                img_type="ico",
                html_code="<link rel='icon' sizes='64x64' href='"+convFileName+"-32x32.ico'>"
            )            
            gen_favicon_ico.path.name=os.path.join(relativePathToConvertedFiles,convFileName+'-32x32.ico')
            gen_favicon_ico.save()
            
            
            # CREATE HTML_CODE.TXT FILE
            html_codes = [
                "<link rel='icon' sizes='64x64' href='"+convFileName+"-64x64.png'>\n",
                "<link rel='icon' sizes='64x64' href='"+convFileName+"-64x64.jpg'>\n",
                "<link rel='icon' sizes='32x32' href='"+convFileName+"-32x32.ico'>\n",
            ]
            ftxt = open(pathToConvertedFiles+"/html_codes.txt", "a")            
            for code in html_codes:
                ftxt.write(code)            
            ftxt.close()


            # Delete uploaded file
            uploadedImgObj.delete()
            # my_zip = zipfile.ZipFile(pathToConvertedFiles+"/"+convFileName+'.zip', 'w')            
            my_zip.write(pathToConvertedFiles+"/"+convFileName+"-64x64.png", arcname=os.path.join(pathToConvertedFiles.replace(pathToConvertedFiles, ""), convFileName+"-64x64.png"))
            my_zip.write(pathToConvertedFiles+"/"+convFileName+"-64x64.jpg", arcname=os.path.join(pathToConvertedFiles.replace(pathToConvertedFiles, ""), convFileName+"-64x64.jpg"))
            my_zip.write(pathToConvertedFiles+"/"+convFileName+"-32x32.ico", arcname=os.path.join(pathToConvertedFiles.replace(pathToConvertedFiles, ""), convFileName+"-32x32.ico"))
            my_zip.write(pathToConvertedFiles+"/html_codes.txt", arcname=os.path.join(pathToConvertedFiles.replace(pathToConvertedFiles, ""),"html_codes.txt"))
            my_zip.close()
        
            # return JsonResponse({"filelink":gen_zipfile.path.url})
            
            zip_toDownload = open(os.path.join(pathToConvertedFiles,mainName+'.zip'), 'rb')
            response = FileResponse(zip_toDownload, mainName+'.zip') 
            # response['Content-Disposition'] = 'attachment; filename="' + mainName + '.zip"'
            return response

            # return render(request, 'main/success.html', {"filelink":gen_zipfile.path, 
            #                                             "statusMessage":"Successfully converted favicon!",
            #                                             "goBack":"/converter_page"})

        except KeyError:
            return redirect('error_w')

    return render(request, 'main/converter.html')
























# START:for_download_tuto
# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'ro') as fh:
#             response = HttpResponse(fh.read(), content_type="application/adminupload")
#             response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
#             return response
    
#     raise Http404
# END:for_download_tuto


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})



def success(request, filelink):
    return render(request, 'main/success.html', {"filelink":filelink})
	# return HttpResponse('Successfully generated favicon!')

def error_w(request):
	return HttpResponse('There was an error !')