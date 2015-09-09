$("form.extract").submit(function(event){
	event.preventDefault(); // don't refresh page

	var inputs = $(this).serializeArray(); // for some reason, returns an array of objects
	var formObj = {};
	for (var i = 0; i < inputs.length; i++)
		formObj[inputs[i].name] = inputs[i].value;

    $.get("/extract", formObj, function(response){
        console.log(response);
        if (response !== ""){
            $("img.meme").attr("src", $(".extract input[name=url]").val());
            $(".text").text(response);
        }
        else {
            alert("Could not extract text from this meme");
        }
    }).fail(function(jqXHR, textStatus, errorThrown){
        alert([textStatus, errorThrown]);
    });
});