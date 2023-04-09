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

function get_students() {
    $.ajax({
        url: "/api/attendance",
        type: "GET",
        dataType: "json",
        success: function(data) {
            show_students(data)
        },
        error: function(data) {
            console.log("Error: " + data)
        }
    })
}

function show_students(student_info) {
        $("#attendancePresent").empty()
        $("#attendanceAbsent").empty()
        for(student of student_info["students"]) {
            if (student["status"] == 1 ) {
                $("#attendancePresent").append(`<li> ${student["name"]} </li>`)
            }
            else {
                $("#attendanceAbsent").append(`<li> ${student["name"]} </li>`)
            }
        }
}

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
        alert("Please enter a valid URL");
      }
    }
