var BUILDING_DATA = {
	floors: {
		'floor1': {
			name: 'Floor 1'
		},
		'floor2':{
			name: 'Floor 2'
		}
	},
	rooms: {
		'room1': {
			name: 'Room 1',
			floor: 'floor1'
		},
		'roomj': {
			name: 'Meeting Room',
			floor: 'floor2'
		}
	}
}

var SENSOR_DATA = {
	'sensor1': {
		open: true,
		room: 'room1'
	},
	'sensor2': {
		open: false,
		room: 'room1'
	},
	'sensor3': {
		open: false,
		room: 'roomj'
	},
	'sensor4': {
		open: true,
		room: 'room1'
	}
}

function getTag(tag, content, opt){
	var classList = false;
	if(opt){
		if(opt.classes){
			classList = ' class="' + opt.classes.join(' ') + '"';
		}
	}
	return '<' + tag + (classList ? classList : '') + '>' + content + '</' + tag + '>';
}

function MapToList(map, mapper, sorter){
	var list = Object.keys(map).map(function(key){
		if(mapper){
			return mapper(map[key], key);	
		}
		else{
			return map[key];
		}
	});
	if(sorter){
		list = list.sort(sorter);
	}
	return list;
}

function constructBuilding(bData, sData){
	var resData = {
		floors: {}
	}
	var directory = {};
	for(var f in bData.floors){
		var floor = bData.floors[f]
		resData.floors[f] = {
			name: floor.name,
			rooms: {}
		}
	}
	for(var r in bData.rooms){
		var room = bData.rooms[r];
		directory[r] = room.floor;
		resData.floors[room.floor].rooms[r] = {
			name: room.name,
			spots: {}
		}
	}
	for(var s in sData){
		var sensor = sData[s];
		resData.floors[directory[sensor.room]].rooms[sensor.room].spots[s] = {
			open: sensor.open
		}
	}
	resData.floors = MapToList(resData.floors, function(floor){
		floor.rooms = MapToList(floor.rooms, function(room){
			room.spots = MapToList(room.spots, function(spot){
				return spot;
			});
			return room;
		});
		return floor;
	})
	return resData;
}

function getHTML(data){
	var html = '';
	for(var f = 0; f < data.floors.length; f++){
		var floor = data.floors[f];
		html += getTag('h1', floor.name);
		for(var r = 0; r < floor.rooms.length; r++){
			var room = floor.rooms[r];
			var spotHTML = getTag('h2', room.name);
			room.spots.forEach(function(a){
				var aH = getTag('spot', a.open ? 'Y' : 'N', {
					classes: [a.open ? 'open' : 'taken']
				});
				spotHTML += aH;
			});
			html += getTag('room', spotHTML);
		}
	}
	return html;
}

var db = firebase.database();
db.ref().on('value', function(snapshot){
	var val = snapshot.val();
	console.log(val);
	var inData = constructBuilding({
		floors: val.floors,
		rooms: val.rooms
	}, val.sensors);
	var roomHTML = getHTML(inData);
	document.body.innerHTML = roomHTML;
});
