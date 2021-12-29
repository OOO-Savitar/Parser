function getComboA(selectObject) {
  	var value = selectObject.value;  
  	
  	if (value == 1) {
  		let input_box = document.getElementById('Value').type = 'number';
  	}
  	else {
  		let input_box = document.getElementById('Value').type = 'text';
  	}
};

function ShowForm(selectCard) {
	let form = document.getElementById('form-card')
	let thisElement = document.getElementsByClassName(selectCard.id)[0]
	var link_img = thisElement.children[0].children[0].src
	console.log(thisElement)
	form.children[0].children[0].children[1].children[0].src = link_img
	form.style.cssText = 'display: block;' 
}

function closeForm() {
	let form = document.getElementById('form-card')
	form.style.cssText = 'display: none;'
}

function Check() {
	let selected = document.getElementById('selectedValue')
	let input_box = document.getElementById('Value');
	
	if (selected.value == 1) {
		if (input_box.value < 0) {
			alert('Введите корректный id')
		}
	}
}