const navbarToggle = navbar.querySelector('#navbar-toggle');
let isNavbarExpanded = navbarToggle.getAttribute('aria-expanded') === 'true';

const toggleNavbarVisibility = () => {
  isNavbarExpanded = !isNavbarExpanded;
  navbarToggle.setAttribute('aria-expanded', isNavbarExpanded);
};

navbarToggle.addEventListener('click', toggleNavbarVisibility);

const navbarMenu = document.querySelector('#navbar-menu');
const navbarLinksContainer = navbarMenu.querySelector('.navbar-links');

navbarLinksContainer.addEventListener('click', (e) => e.stopPropagation());
navbarMenu.addEventListener('click', toggleNavbarVisibility);

    function generateQRCode() {
      let website = document.getElementById("website").value;
      if (website) {
        let qrcodeContainer = document.getElementById("qrcode");
        qrcodeContainer.innerHTML = "";
        new QRCode(qrcodeContainer, website);
        /*With some styles*/
        let qrcodeContainer2 = document.getElementById("qrcode-2");
        qrcodeContainer2.innerHTML = "";
        new QRCode(qrcodeContainer2, {
          text: website,
          width: 128,
          height: 128,
          colorDark: "#5868bf",
          colorLight: "#ffffff",
          correctLevel: QRCode.CorrectLevel.H
        });
        document.getElementById("qrcode-container").style.display = "block";
      } else {
      }
    }

function submitData() {
  const form = document.getElementById('myForm');
  const formData = new FormData(form);

  axios.post('/les', formData)
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
}

 const form = document.querySelector("#attendance-form");

        form.addEventListener("submit", (event) => {
            event.preventDefault();
            const data = {
                user_id: form.user_id.value,
                class_id: form.class_id.value
            };
            fetch("/studenthome", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }).then(response => {
                console.log(response.json());
            }).catch(error => {
                console.error(error);
            });
        });

$(document).ready(function() {
    // Haal lessen op en vul het selectie-element
    $.ajax({
        url: '/lessons',
        type: 'GET',
        success: function(data) {
            var lessonSelect = $('#lessonSelect');
            $.each(data, function(index, lesson) {
                lessonSelect.append($('<option>', {
                    value: lesson.id,
                    text: lesson.name
                }));
            });
        },
        error: function(error) {
            console.error('Fout bij het ophalen van lessen:', error);
        }
    });

    // Verwerk het formulier voor het toevoegen van lessen
    $('#lessonForm').submit(function(event) {
        event.preventDefault();

        var Name = $('#Name').val();

        $.ajax({
            url: '/add_lesson',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ "name": name }),
            success: function(data) {
                console.log(data.message);
                // Voeg hier eventueel verdere verwerking toe
            },
            error: function(error) {
                console.error('Fout bij het toevoegen van de les:', error);
            }
        });
    });

    // Verwerk het klikken op de knop voor het ophalen van aanwezigheidsgegevens
    $('#getAttendanceBtn').click(function() {
        var lessonId = $('#lessonSelect').val();

        $.ajax({
            url: '/attendance/' + lessonId,
            type: 'GET',
            success: function(data) {
                var attendanceTableBody = $('#attendanceTableBody');
                attendanceTableBody.empty();

                $.each(data.attendance_data, function(index, row) {
                    var studentNaam = row.name;
                    var status = row.status;

                    var tr = $('<tr>');
                    var tdName = $('<td>').text(studentNaam);
                    var tdStatus = $('<td>').text(status);
                    tr.append(tdName, tdStatus);
                    attendanceTableBody.append(tr);
                });
            },
            error: function(error) {
                console.error('Fout bij het ophalen van de aanwezigheidsgegevens:', error);
            }
        });
    });
});

submitData()
