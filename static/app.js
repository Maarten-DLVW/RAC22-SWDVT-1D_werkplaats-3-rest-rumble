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