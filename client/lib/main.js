var ROOM_DATA = {
	floors: [{
		name: 'Floor 1',
		rooms: [{
			name: 'Room 1',
			spots: [{
				open: true,
				sensor: 'sensor1'
			}, {
				open: false,
				sensor: 'sensor2'
			}]
		}, {
			name: 'Room 2',
			spots: [{
				open: false,
				sensor: 'sensor3'
			}, {
				open: false,
				sensor: 'sensor4'
			}, {
				open: false,
				sensor: 'sensor5'
			}]
		}]
	}, {
		name: 'Floor 2',
		rooms: [{
			name: 'Conference Room',
			spots: [{
				open: false,
				sensor: 'sensor1'
			}, {
				open: false,
				sensor: 'sensor2'
			}]
		}]
	}]
}

function getTag(tag, content){
	return '<' + tag + '>' + content + '</' + tag + '>';
}

function getHTML(data){
	var html = '';
	for(var f = 0; f < data.floors.length; f++){
		var floor = data.floors[f];
		html += getTag('h1', floor.name);
		for(var r = 0; r < floor.rooms.length; r++){
			var room = floor.rooms[r];
			var spotHTML = getTag('h2', room.name);
			spotHTML += room.spots.reduce(function(a, b){
				var aH = getTag('spot', a.open ? 'Y' : 'N');
				var bH = getTag('spot', b.open ? 'Y' : 'N');
				return aH + bH;
			});
			html += getTag('room', spotHTML);
		}
	}
	return html;
}

var roomHTML = getHTML(ROOM_DATA);
document.body.innerHTML = roomHTML;