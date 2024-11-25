// Handle Next Step
function nextStep(currentStep) {
    var steps = document.querySelectorAll('.step');
    var currentIndex = Array.from(steps).indexOf(currentStep);
    if (currentIndex + 1 < steps.length) {
        steps[currentIndex].classList.remove('active');
        steps[currentIndex + 1].classList.add('active');
        updateProgressBar(currentIndex + 1);
    }
}

// Handle Previous Step
function prevStep(currentStep) {
    var steps = document.querySelectorAll('.step');
    var currentIndex = Array.from(steps).indexOf(currentStep);
    if (currentIndex - 1 >= 0) {
        steps[currentIndex].classList.remove('active');
        steps[currentIndex - 1].classList.add('active');
        updateProgressBar(currentIndex - 1);
    }
}

// Update the Progress Bar
function updateProgressBar(stepIndex) {
    var progressBar = document.querySelector('.progress-bar');
    var progressDots = progressBar.querySelectorAll('span');
    progressDots.forEach((dot, index) => {
        if (index <= stepIndex) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

// Handle File Input Change (for better UX)
document.querySelectorAll('input[type="file"]').forEach(input => {
    input.addEventListener('change', function() {
        var fileName = this.files.length > 0 ? this.files[0].name : 'No file selected';
        var label = this.previousElementSibling;
        label.textContent = 'Browse for Photo (' + fileName + ')';
    });
});
