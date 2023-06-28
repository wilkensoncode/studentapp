function delete_note(noteId) {
    fetch('/delete_note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = '/profile'
    });
}

setTimeout( () => {
    document.querySelector('#flash_message_for_five_second').style.display ='none'
}, 4500)
 