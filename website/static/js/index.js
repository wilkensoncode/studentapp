function delete_note(noteId) {
    fetch('/delete_note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = '/profile'
    });
}

function showStudents() {
    fetch('/delete_note', {
        method: 'POST',
        body: JSON.stringify()
    }).then((_res) => {
        window.location.href = '/'
    });
}

function shoowClubs() {
    fetch('/', {
        method: 'POST',
        body: JSON.stringify( )
    }).then((_res) => {
        window.location.href = '/'
    });
}

function showCourses() {
    fetch('/', {
        method: 'POST',
        body: JSON.stringify( )
    }).then((_res) => {
        window.location.href = '/'
    });
}

setTimeout( () => {
    document.querySelector('#flash_message_for_five_second').style.display ='none'
}, 4500)
 