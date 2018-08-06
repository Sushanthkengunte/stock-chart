
$("#progress").hide();


$("#reset").click(function() {

  $("#chart").empty();
});


// client side validation
function validateDate(startYear,endYear){


  if(startYear.trim().length == 0)
    startYear = "1980";

   var currentTime = new Date()
  if(endYear.trim().length == 0){

    endYear = currentTime.getFullYear().toString();
  }


  var start = parseInt(startYear.trim(),10);
  var end = parseInt(endYear.trim(),10);
  

  if(startYear>endYear || startYear<1980 || endYear>currentTime.getFullYear() ){
    alert("Please enter the correct years between 1980 to now");
    return {result: false,startYear: "0",endYear:"0"};
  }

  return {result:true,startYear:startYear,endYear:endYear};

}


$("#drawPlot").click(function() {

  var startYear = $('input:text[name=start]').val();
  var endYear = $('input:text[name=end]').val();
  

  var companyName = $('input:radio[name=company]:checked').val();
  var validateDatedOutcome = validateDate(startYear,endYear);


  if(validateDatedOutcome.result){

        $("#progress").show();
        $("#chart").hide();

        var display = {"companyName":companyName,"startYear":validateDatedOutcome.startYear,"endYear":validateDatedOutcome.endYear}


        $.ajax({
          type: "POST",
          async:true,
          contentType: "application/json; charset=utf-8",
          url: "/stockChart",
          data: JSON.stringify(display),
          success: function (data) {     
           var graph = $("#chart");
           graph.html(data);
            $("#progress").hide();
           $("#chart").show();
         },
         dataType: "html"
       });
    }
    });
