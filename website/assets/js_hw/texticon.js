document.addEventListener('DOMContentLoaded', () => {

    // console.log("TEXTICON JS FILE IS LOADED")

    // *************************************************************

    var slider1 = document.getElementById("myRange");
    var output = document.getElementById("range_output_hw");
    var texticonDiv = document.getElementById("texticon_preview_hw");
    var texticonInput = document.getElementById("texticon_input_hw");
    var texticonBgShape = document.getElementById("texticon_bg_shape_hw");
    var texticonFonts = document.getElementById("texticon_fonts_hw");
    var texticonFontColor = document.getElementById("texticon_font_color_hw");
    var texticonBgColor = document.getElementById("texticon_bg_color_hw");
    var texticonBorderColor = document.getElementById("texticon_border_color_hw");
    var downloadTexticonBtn = document.getElementById("download_texticon_btn");

    var svgContent = document.getElementById("sgenerator_svg_content");

    // Svg elements to edit
    var texticonSvgRect = texticonDiv.children[0].children[1];
    var texticonSvgText = texticonDiv.children[0].children[2];

    // State 0
    output.innerHTML = slider1.value;
    texticonSvgText.setAttribute('font-size', slider1.value)

    texticonSvgText.innerHTML = texticonInput.value;

    texticonSvgText.setAttribute('style', `font-family:${texticonFonts.value}`)

    texticonSvgText.setAttribute('fill', texticonFontColor.value)

    texticonSvgRect.setAttribute('fill', texticonBgColor.value)

    texticonSvgRect.setAttribute('stroke', texticonBorderColor.value)

    switch (texticonBgShape.value) {
        case "Rounded":
            texticonSvgRect.setAttribute('rx', 15);
            texticonSvgRect.setAttribute('ry', 15);
            break;
        case "Square":
            texticonSvgRect.setAttribute('rx', 0);
            texticonSvgRect.setAttribute('ry', 0);
            break;
        case "Circle":
            texticonSvgRect.setAttribute('rx', 32);
            texticonSvgRect.setAttribute('ry', 32);
            break;
        
        default:
            break;
    }


    // Events actions
    slider1.oninput = function() {
        output.innerHTML = this.value;
        texticonSvgText.setAttribute('font-size', this.value)
    }

    texticonInput.oninput = function() {
        texticonSvgText.innerHTML = this.value;
    }

    texticonBgShape.onchange = function() {
        switch (this.value) {
            case "Rounded":
                texticonSvgRect.setAttribute('rx', 15);
                texticonSvgRect.setAttribute('ry', 15);
                break;
            case "Square":
                texticonSvgRect.setAttribute('rx', 0);
                texticonSvgRect.setAttribute('ry', 0);
                break;
            case "Circle":
                texticonSvgRect.setAttribute('rx', 32);
                texticonSvgRect.setAttribute('ry', 32);
                break;
            
            default:
                break;
        }
    }
    texticonFonts.onchange = function() {
        texticonSvgText.setAttribute('style', `font-family:${this.value}`)
    }
    texticonFontColor.oninput = function() {
        texticonSvgText.setAttribute('fill', this.value)
    }
    texticonBgColor.oninput = function() {
        texticonSvgRect.setAttribute('fill', this.value)
    }
    texticonBorderColor.oninput = function() {
        texticonSvgRect.setAttribute('stroke', this.value)
    }


    // SUBMIT DESIGNED FAVICON
    downloadTexticonBtn.onclick = function (e) { 
        e.preventDefault();
        var texticonSvg = `${texticonDiv.innerHTML}`;
        svgContent.setAttribute('value', texticonSvg);        
        console.log(texticonSvg)
        document.forms[0].submit();
        return false;
    }



});