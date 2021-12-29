function getComboA(selectObject) {
  	var value = selectObject.value;  
  	
  	if (value == 1) {
  		let input_box = document.getElementById('Value').type = 'number';
  	}
  	else {
  		let input_box = document.getElementById('Value').type = 'text';
  	}
};

window.onload = function() {
	let input_box = document.getElementById('Value').type = 'number';
}

function ShowForm(selectCard) {
	alert(selectCard)
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