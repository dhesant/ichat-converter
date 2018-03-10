$(document).on('change', '#customFile', function(event) {
    var reader = new FileReader();
    
    reader.onload = function(event) {
	var jsonObj = JSON.parse(event.target.result);
	parse_ichat(jsonObj);
    }
    
    reader.readAsText(event.target.files[0]);
});

function parse_ichat(jsonObj) {
    console.log(jsonObj['NS.objects']);

    $("#info").empty();
    $("#viewer").empty();

    $("#info").append('<p class="mr-2">Protocol: ' + jsonObj['NS.objects'][0] + '</p>');
    $("#info").append('<p class="mr-2">Participants: ' + jsonObj['NS.objects'][5] + '</p>');
    
    _.each(jsonObj['NS.objects'][3], function(usr, index) {
	$("#info").append('<p class="mr-2">Participant ' + (index + 1) + ': ' + usr['ID'])
    });
    
    _.each(jsonObj['NS.objects'][2], function(msg, index) {
	if (msg['Sender'] === null) {
	    var elem  = $('<span class="system-message">' + msg['Time'] + ': ' + msg['OriginalMessage'] + '</span>')
	}
	else {
	    var elem = $('<span class="message">' + msg['OriginalMessage'] + '</span>')
	    
	    if (msg['Sender']['ID'] == msg['Sender']['ServiceLoginID']) {
		elem.addClass("host-message");
		$("#viewer").append(elem);
	    }
	    else {
		var usrname = $('<span class="username">' + msg['Sender']['ID'] + '</span>');
		elem.addClass("guest-message");
		$("#viewer").append(usrname).append(elem);

	    }
	}
    });
}
