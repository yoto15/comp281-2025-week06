
document.addEventListener("DOMContentLoaded", main);

function main() {
	const nameInput = document.querySelector('#name');
	const sendButton = document.querySelector('#send');
	const output = document.querySelector('#output');
	sendButton.addEventListener('click', function() {
		const name = nameInput.value;
		
		fetch('/action', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ name: name })
		})
		.then(response => response.json())
		.then(data => {
			output.value = `${data.message}\nData = ${data.received_data}`;
			console.log(data);
		});
	});
}