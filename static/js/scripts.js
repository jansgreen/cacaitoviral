
$(document).ready(function () {
  $(".toast").toast("show");
});

/* autenticar al usuario y realizar like*/
function authenticate() {
  console.log("ESTA FUNCIONANDO")
  return gapi.auth2.getAuthInstance()
    .signIn({ scope: "https://www.googleapis.com/auth/youtube https://www.googleapis.com/auth/youtube.force-ssl https://www.googleapis.com/auth/youtubepartner" })
    .then(function () { console.log("Sign-in successful"); },
      function (err) { console.error("Error signing in", err); });
}
function loadClient() {
  gapi.client.setApiKey("AIzaSyDoL-_pWJuQL7D82T8kmTOO7ni5fQTETC8");
  return gapi.client.load("https://content.googleapis.com/discovery/v1/apis/youtube/v3/rest")
    .then(function () { console.log("GAPI client loaded for API"); },
      function (err) { console.error("Error loading GAPI client for API", err); });
}
// Make sure the client is loaded and sign-in is complete before calling this method.
function Alike() {
  video_ID = document.getElementById('Video_ID').value
  console.log(video_ID)
  return gapi.client.youtube.videos.rate({
    "id": "79DijItQXMM",
    "rating": "like",
    "callback": "http://http://127.0.0.1:8000/accounts/google/login/callback/"
  })
    .then(function (response) {
      // Handle the results here (response.result has the parsed body).
      console.log("Response", response);
    },
      function (err) { console.error("Execute error", err); });
}
gapi.load("client:auth2", function () {
  gapi.auth2.init({ client_id: "658919410948-1ft0h1ujbpim40vsaj68fkifm1cs44s1.apps.googleusercontent.com" });
});

function Suscriptcion() {
  return gapi.client.youtube.subscriptions.insert({
    "resource": {
      "id": ""
    }
  })
      .then(function(response) {
              // Handle the results here (response.result has the parsed body).
              console.log("Response", response);
            },
            function(err) { console.error("Execute error", err); });
}
gapi.load("client:auth2", function() {
  gapi.auth2.init({client_id: "YOUR_CLIENT_ID"});
});


/*SUSCRIPCIONES */
function addSubscription() {
  // Replace this channel ID with the channel ID you want to subscribe to
  Canal = document.getElementById("Id_Canal");

  var channelId = Canal;
  var resource = {
    snippet: {
      resourceId: {
        kind: 'youtube#channel',
        channelId: channelId
      }
    }
  };

  try {
    var response = YouTube.Subscriptions.insert(resource, 'snippet');
    Logger.log(response);
  } catch (e) {
    if(e.message.match('subscriptionDuplicate')) {
      Logger.log('Cannot subscribe; already subscribed to channel: ' + channelId);
    } else {
      Logger.log('Error adding subscription: ' + e.message);
    }
  }
}


/* BARRA DE PROGRESO*/

$(document).ready(function () {
  progress = document.getElementById("progress-id");
  const div = document.createElement("DIV");
  div.setAttribute("class", "progress-bar progress-bar-striped");
  div.setAttribute("role", "progressbar");
  div.setAttribute("style", "width: 3.2%");
  div.setAttribute("aria-valuenow", "10");
  progress.appendChild(div)
  Tiempo = document.getElementById("Tiempo").value;
  progreso = (Tiempo/100)
  console.log(progreso)

  const fileReader = new FileReader();
  fileReader.readAsDataURL()

});
