const BASE_URL = 'http://localhost:5000/api';
$('#alert').hide();

const createHTML = (cupcake) => {
  return `
    <div data-id="${cupcake.id}"class="card" style="width: 18rem;">
    <img class="card-img-top" src="${cupcake.image}" alt="Card image cap">
    <div class="card-body">
        <h5 class="card-title">${cupcake.flavor}</h5>
        <p class="card-text">${cupcake.size}</p>
        <p class="card-text">${cupcake.rating}</p>
        <a href="#" class="btn btn-danger">Delete</a>
    </div>
    </div>
  `;
};

const showCupcakes = async () => {
  const res = await axios.get(`${BASE_URL}/cupcakes`);
  for (let cupcake of res.data.cupcakes) {
    let newCupcake = $(createHTML(cupcake));
    $('#cupcakes-list').append(newCupcake);
  }
};

$('#cupcake-form').on('submit', async function (evt) {
  evt.preventDefault();

  let flavor = $('#flavor').val();
  let rating = $('#rating').val();
  let size = $('#size').val();
  let image = $('#image').val();

  $('#alert').empty();

  if (!flavor || !rating || !size) {
    $('#alert')
      .fadeIn()
      .append('Please fill our form completely')
      .delay(3000)
      .fadeOut();
  }

  const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
    flavor,
    rating,
    size,
    image,
  });

  let newCupcake = $(createHTML(newCupcakeResponse.data.cupcake));
  $('#cupcakes-list').append(newCupcake);
  $('#cupcake-form').trigger('reset');
});

$('#cupcakes-list').on('click', '.btn-danger', async function (e) {
  e.preventDefault();
  let $parent = $(e.target).closest('.card');
  let cupcake = $parent.attr('data-id');

  await axios.delete(`${BASE_URL}/cupcakes/${cupcake}`);
  $parent.remove();
});

showCupcakes();
