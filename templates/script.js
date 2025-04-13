// Script to handle modal functionality
document.addEventListener('DOMContentLoaded', () => {
  const modals = document.querySelectorAll('.modal');
  const closeButtons = document.querySelectorAll('.close');

  // Open modals
  document.querySelectorAll('.service-item').forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const target = item.getAttribute('href');
      document.querySelector(target).style.display = 'block';
    });
  });

  // Close modals
  closeButtons.forEach(button => {
    button.addEventListener('click', () => {
      button.closest('.modal').style.display = 'none';
    });
  });

  // Close modals when clicking outside of modal content
  window.addEventListener('click', (event) => {
    modals.forEach(modal => {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    });
  });

  // Handle form submissions
  document.getElementById('caseFiling').onsubmit = (event) => {
    event.preventDefault();
    console.log('Case Filing Form submitted');
    alert('Case filed successfully');
    document.getElementById('caseFiling').reset();
    document.getElementById('caseFilingForm').style.display = 'none';
  };

  document.getElementById('caseStatusTracking').onsubmit = (event) => {
    event.preventDefault();
    console.log('Case Status Tracking Form submitted');
    alert('Tracking case status');
    document.getElementById('caseStatusTracking').reset();
    document.getElementById('caseStatusForm').style.display = 'none';
  };

  document.getElementById('legalResources').onsubmit = (event) => {
    event.preventDefault();
    console.log('Legal Resources Form submitted');
    alert('Searching legal resources');
    document.getElementById('legalResources').reset();
    document.getElementById('legalResourcesForm').style.display = 'none';
  };

  document.getElementById('onlineConsultation').onsubmit = (event) => {
    event.preventDefault();
    console.log('Online Consultation Form submitted');
    alert('Submitting query for consultation');
    document.getElementById('onlineConsultation').reset();
    document.getElementById('onlineConsultationForm').style.display = 'none';
  };
  
  // Handle feedback button and form submission
  const feedbackBtn = document.getElementById('feedbackBtn');
  const feedbackModal = document.getElementById('feedbackModal');
  feedbackBtn.addEventListener('click', () => {
    feedbackModal.style.display = 'block';
  });

  document.getElementById('feedbackForm').onsubmit = (event) => {
    event.preventDefault();
    console.log('Feedback Form submitted');
    alert('Thank you for your feedback');
    document.getElementById('feedbackForm').reset();
    feedbackModal.style.display = 'none';
  };
});

