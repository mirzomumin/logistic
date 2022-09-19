$("#id_state").change(function () {
  // var url = $("#ajax_load_cities").attr("href");  // get the url of the `load_cities` view
  var protocol = window.location.protocol
  var host = window.location.host
  var url = protocol + '//' + host + '/ajax/load-cities/'
  console.log(url)
  var stateId = $(this).val();  // get the selected country ID from the HTML input

  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
    data: {
      'state': stateId,       // add the country id to the GET parameters
      csrfmiddlewaretoken: '{{ csrf_token }}'
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server
      console.log(data)
    },
  });

});