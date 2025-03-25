document.addEventListener('DOMContentLoaded', function () {
    // Handle star ratings
    document.querySelectorAll('.rating-stars').forEach(container => {
      const stars = container.querySelectorAll('.star-icon');
      let selectedRating = 0;
  
      stars.forEach((star, index) => {
        star.addEventListener('mouseover', () => {
          stars.forEach((s, i) => {
            s.classList.toggle('fa-solid', i <= index);
            s.classList.toggle('fa-regular', i > index);
          });
        });
  
        star.addEventListener('click', () => {
          selectedRating = index + 1;
          container.setAttribute('data-selected', selectedRating);
        });
  
        star.addEventListener('mouseout', () => {
          let rating = container.getAttribute('data-selected') || 0;
          stars.forEach((s, i) => {
            s.classList.toggle('fa-solid', i < rating);
            s.classList.toggle('fa-regular', i >= rating);
          });
        });
      });
    });
  
    // Save Recipe button event
    document.querySelectorAll('.save-btn').forEach(button => {
      button.addEventListener('click', () => {
        const recipeId = button.getAttribute('data-recipe-id');
        saveRecipe(recipeId, button);
      });
    });
  
    // Submit Rating button event
    document.querySelectorAll('.submit-rating-btn').forEach(button => {
      button.addEventListener('click', () => {
        const recipeId = button.getAttribute('data-recipe-id');
        submitRating(recipeId, button);
      });
    });

    // Hide save and rate buttons if user is not authenticated
    document.querySelector("div[data-user-authenticated=False]").style.display = "none";
  });
  
  function submitRating(recipeId, button) {
    const container = document.querySelector(`.rating-stars[data-recipe-id='${recipeId}']`);
    const rating = container.getAttribute('data-selected');
  
    if (!rating) {
      alert("Please select a rating.");
      return;
    }
  
    console.log(`Submitting rating ${rating} for recipe ${recipeId}`);
  
    // Optional AJAX call
    /*
    fetch(`/rate-recipe/${recipeId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify({ rating: rating })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        button.textContent = "Rated!";
        button.classList.remove("btn-success");
        button.classList.add("btn-secondary");
        button.disabled = true;
      }
    });
    */
  
    // Simulated result for now
    button.textContent = "Rated!";
    button.classList.remove("btn-success");
    button.classList.add("btn-secondary");
    button.disabled = true;
  }
  
  function saveRecipe(recipeId, button) {
    fetch(`/save-recipe/${recipeId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        button.textContent = "Saved!";
        button.classList.remove("btn-outline-primary");
        button.classList.add("btn-success");
        button.disabled = true;
      } else {
        alert(data.message || "Could not save recipe.");
      }
    })
    .catch(err => {
      console.error("Error saving recipe:", err);
      alert("Something went wrong.");
    });
  }
  
  function getCSRFToken() {
    let cookieValue = null;
    const name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
