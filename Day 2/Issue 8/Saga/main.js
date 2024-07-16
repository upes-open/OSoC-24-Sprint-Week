document.addEventListener('DOMContentLoaded', () => {

    const fileInput = document.querySelector('#image-input');
    const canvas = document.querySelector('#canvas');
    const canvasCtx = canvas.getContext("2d");
    const brightnessInput = document.querySelector('#brightness');
    const contrastInput = document.querySelector('#contrast');
    const inversionInput = document.querySelector('#inversion');
    const saturationInput = document.querySelector('#saturation');
    const blurInput = document.querySelector('#blur');

    const settings = {};
    let image = null;

    function resetSettings() {
        settings.brightness = "100";
        settings.contrast = "100";
        settings.inversion = "0";
        settings.saturation = "100";
        settings.blur = "0";

        brightnessInput.value = settings.brightness;
        contrastInput.value = settings.contrast;
        inversionInput.value = settings.inversion;
        saturationInput.value = settings.saturation;
        blurInput.value = settings.blur;
    }

    function updateSettings(key, value) {
        if (!image) return;

        settings[key] = value;
        renderImage();
    }

    function generateFilter() {
        const { brightness, contrast, inversion, saturation, blur } = settings;

        return `brightness(${brightness}%) contrast(${contrast}%) invert(${inversion}%) saturate(${saturation}%) blur(${blur}px)`
    }

    function renderImage() {
        canvas.width = image.width;
        canvas.height = image.height;

        canvasCtx.filter = generateFilter();
        canvasCtx.drawImage(image, 0, 0);
    }

    brightnessInput.addEventListener("change", () => { updateSettings("brightness", brightnessInput.value) });
    contrastInput.addEventListener("change", () => { updateSettings("contrast", contrastInput.value) });
    inversionInput.addEventListener("change", () => { updateSettings("inversion", inversionInput.value) });
    saturationInput.addEventListener("change", () => { updateSettings("saturation", saturationInput.value) });
    blurInput.addEventListener("change", () => { updateSettings("blur", blurInput.value) });

    fileInput.addEventListener("change", () => {
        image = new Image();

        image.addEventListener("load", () => {
            resetSettings();
            renderImage();
        });

        image.src = URL.createObjectURL(fileInput.files[0]);

    })

    resetSettings();
});
