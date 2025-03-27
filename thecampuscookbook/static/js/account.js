$(document).ready(() => {
  // Remove a saved recipe from the user's saved recipes.
    $('.remove-button').click(function() {
       recipe_id = $(this).attr('data-recipe-id')
       $.ajax({
        url: '/recipe/remove/',
        method: 'POST',
        dataType: "json",
        data: JSON.stringify({ "recipeId": `${recipe_id}` }),
        headers: { "X-CSRFToken": getCSRFToken(), "X-Requested-With": "XMLHttpRequest" },
        credentials: 'same-origin',
        success: function (response) {
            // Go to parent card, then remove the card/hide it from view.
            switch(response.status) {
                case 'removed':
                    hideDeletedCard(recipe_id);
                    break;
            }
        },
        error: function (xhr, status, error) {
          console.error('Error:', error);
          // Show message that already rated.
          console.log(status)
          alert("You have already removed this recipe.");
        }
      });
    })


    // Delete recipe when delete button is clicked.
    $('.recipe-delete-button').click(function() {
       recipe_id = $(this).attr('data-recipe-id')
       $.ajax({
        url: '/recipe/delete/',
        method: 'POST',
        dataType: "json",
        data: JSON.stringify({ "recipeId": `${recipe_id}` }),
        headers: { "X-CSRFToken": getCSRFToken(), "X-Requested-With": "XMLHttpRequest" },
        credentials: 'same-origin',
        success: function (response) {
            // Go to parent card, then remove the card/hide it from view.
            switch(response.status) {
                case 'deleted':
                    hideDeletedCard(recipe_id);
                    break;
            }
        },
        error: function (xhr, status, error) {
          console.error('Error:', error);
          // Show message that already rated.
          console.log(status)
          alert("Could not delete recipe.");
        }
      });
    })
})

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


  function hideDeletedCard(recipe_id) {
    $('.recipe-card').each((index, card) => {
        console.log(card);
        if ($(card).attr('data-recipe-id') == recipe_id) {
            $(card).hide()
        }
    })
  }

