$(document).ready(function () {
  $(".increment-btn").click(function (e) {
    e.preventDefault();

    var inc_value = $(this).closest(".product-data").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product-data").find(".qty-input").val(value);
    }
  });

  $(".decrement-btn").click(function (e) {
    e.preventDefault();

    var dec_value = $(this).closest(".product-data").find(".qty-input").val();
    var value = parseInt(dec_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest(".product-data").find(".qty-input").val(value);
    }
  });

  $(".addToCartBtn").click(function (e) {
    e.preventDefault();
    var produto_id = $(this).closest(".product-data").find(".prod_id").val();
    var produto_qtd = $(this).closest(".product-data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/addcarrinho",
      data: {
        'produto_id': produto_id,
        'produto_qtd': produto_qtd,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        alertify.success(response.status)
      }
    });
  });


  $(".changeQuantity").click(function (e) {
    e.preventDefault();
    var produto_id = $(this).closest(".product-data").find(".prod_id").val();
    var produto_qtd = $(this).closest(".product-data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/updatecarrinho",
      data: {
        'produto_id': produto_id,
        'produto_qtd': produto_qtd,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        // alertify.success(response.status)
      }
    });
  });

  
  $(document).on('click', '.delete-cart-item', function (e) {
     
    e.preventDefault();
    var produto_id = $(this).closest(".product-data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/deletaritemcarrinho",
      data: {
        'produto_id': produto_id,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        // alertify.success(response.status);
        $('.cart-data').load(location.href + " .cart-data");
      }
    });

  });
});
