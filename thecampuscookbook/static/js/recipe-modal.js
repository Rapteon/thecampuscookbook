$(document).ready(function () {
  // Handle star ratings
  $('.rating-stars').each((index, container) => {

    const stars = $(container).children('.star-icon');
    let selectedRating = 0;

    $(stars).each((index, star) => {
      $(star).on('click', () => {
        selectedRating = index + 1;
        $(container).attr('data-selected', selectedRating);

        $(stars).each((i, s) => {
          $(s).toggleClass('fa-solid', i <= index);
          $(s).toggleClass('fa-regular', i > index);
        })
      });
    })

  })

  $('.save-btn').each((index, button) => {
    $(button).click(() => {
      const recipeId = $(button).attr('data-recipe-id');
      saveRecipe(recipeId, button);
    })
  })


  $('.submit-rating-btn').each((index, button) => {
    $(button).click(() => {
      const recipeId = $(button).attr('data-recipe-id');
      submitRating(recipeId, button);
    })
  })

  // Hide save and rate buttons if user is not authenticated
  if ($("div[data-user-authenticated=False]").length > 0) {
    $('.save-btn').hide();
    $('.submit-rating-btn').hide();
    $('.rating-stars').hide();
  }
  else if ($("div[data-user-authenticated=True]").length > 0) {
    $('.save-btn').show();
    $('.submit-rating-btn').show();
    $('.rating-stars').show();
  }
})

function submitRating(recipe_id, button) {
  const rating = $(`.rating-stars[data-recipe-id=${recipe_id}]`).attr('data-selected');

  if (!rating) {
    alert("Please select a rating.");
    return;
  }

  console.log(`Submitting rating ${rating} for recipe ${recipe_id}`);

  $.ajax({
    url: '/recipe/rate/',
    method: 'POST',
    dataType: "json",
    data: JSON.stringify({ "recipeId": `${recipe_id}`, "rating": `${rating}` }),
    headers: { "X-CSRFToken": getCSRFToken(), "X-Requested-With": "XMLHttpRequest" },
    credentials: 'same-origin',
    success: function (response) {
      switch (response.status) {
        case "already rated":
          alert("You have already rated this recipe.");
          break;
        case "rated":
          button.textContent = "Rated!";
          button.classList.remove("btn-success");
          button.classList.add("btn-secondary");
          button.disabled = true;
          updateRecipe(recipe_id);
          break;
      }
    },
    error: function (xhr, status, error) {
      console.error('Error:', error);
      // Show message that already rated.
      console.log(xhr)
    }
  });
}

function saveRecipe(recipeId, button) {
  $.ajax({
    url: '/recipe/save/',
    method: 'POST',
    dataType: "json",
    data: JSON.stringify({ "recipeId": `${recipeId}` }),
    headers: { "X-CSRFToken": getCSRFToken(), "X-Requested-With": "XMLHttpRequest" },
    credentials: 'same-origin',
    success: function (response) {
      // Do someting here.
      switch (response.status) {
        case "saved":
          button.textContent = "Saved!";
          button.classList.remove("btn-outline-primary");
          button.classList.add("btn-success");
          button.disabled = true;
          break;
        case 'already saved':
          alert("You have already saved this recipe.");
          break;
        case 'not found':
          alert("Recipe not found.");
          break;
      }
    },
    error: function (xhr, status, error) {
      console.error('Error:', error);
    }
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

function updateRecipe(recipe_id) {
  $.ajax({
    url: '/recipe/get/',
    method: 'POST',
    dataType: "json",
    data: JSON.stringify({ "recipeId": `${recipe_id}` }),
    headers: { "X-CSRFToken": getCSRFToken(), "X-Requested-With": "XMLHttpRequest" },
    credentials: 'same-origin',
    success: function (response) {
      recipe = JSON.parse(response.recipe)
      console.log(recipe);
      $('.rating').each((index, rating) => {
        console.log("Rating card: ", rating);
        const idToSearch = recipe.id
        const idInCard = $(rating).attr('data-recipe-id')
        console.log(idToSearch, idInCard, typeof idToSearch, typeof idInCard)
        if ($(rating).attr('data-recipe-id') == recipe.id) {
          $(rating).children('.star').each((index, star) => {
            // Reset star display.
            $(star).removeClass('filled');
            $(star).removeClass('empty');
          })
          $(rating).children('.star').each((index, star) => {
            if (index < recipe.average_rating) {
              $(star).addClass('filled');
            }
            else {
              $(star).addClass('empty');
            }
          })
          console.log('Rating card updated: ', rating)
        }
      }
      );
    },
    error: function (xhr, status, error) {
      console.error('Error:', error);
    }
  });
}