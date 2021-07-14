const grandparent = document.querySelector(".grandparent")
const parent = document.querySelector(".parent")
const child = document.querySelector(".child")

grandparent.addEventListener("click",e =>{
	console.log(e)

})


window.addEventListener('DOMContentLoaded', () =>{
    const overlay = document.querySelector('#overlay')
    const delBtn = document.querySelector('#delete-btn')
    const closeBtn = document.querySelector('#close-modal')

    const toggleModal = () => {
        overlay.classList.toggle('hidden')
        overlay.classList.toggle('flex')
    }

    delBtn.addEventListener('click', toggleModal)

    closeBtn.addEventListener('click', toggleModal)
})