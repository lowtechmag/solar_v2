// console.log('script loaded');

let url = "/api/stats.json";  
let data;
let solar_stats = [];
let battery_stats = [];
let general_stats = [];

loadJSON();

async function loadJSON() {
  const response = await fetch(url);
  const data = await response.json();
  setupBatteryMeter(data);
  populateDashboard(data);
  populateForecast(data);

  if (window.location.href.indexOf('/power/') > -1) {
      //load general stats on power page
      populateData(data);
  }  
}


function setupBatteryMeter(data) {
    //setup visible battery level
    let level = parseInt(data.charge);
    let indicator = document.getElementById('battery_data');
    document.getElementById('battery').style.height = (100-level) + '%';
    // indicator.style.top = 100 - parseInt(level) + "vh";
    indicator.style.top = (100-level)  + "vh";

    if (data.charging == "no") {
        // battery is draining, show battery level
        document.getElementById('level').textContent = level;
    } else {
        // sun is out!
        indicator.setAttribute('data-charging', 'yes');
    }

}

function pushData(arr) {
    // returns a list of dt/dd pairs from a two-dimensional array
    let stats = [];
    for (i = 0; i < arr.length; i++) {
        stats.push("<dt>" + arr[i][0] + "</dt><dd>" + arr[i][1] + "</dd>");
    }
    return stats;
}

function populateData(data) {
    let load = ((data.load_15 / 2) * 100).toFixed(2) + '%';

    let general_stats = [
        ["Local time", data.local_time],
        ["Uptime", data.uptime],
        ["Power usage", data.W],
        ["Current draw", data.A],
        ["Voltage", data.V],
        ["CPU temperature", data.temperature + "°C"],
        ["CPU load average *", load],
        ["Solar panel active", data.charging],
        ["Battery capacity", data.charge + "%"]
    ];

    let dl = document.getElementById('server');
    dl.innerHTML = pushData(general_stats).join("");
}


function populateForecast(data) {
    const weather_ignore = ["snow", "sleet", "wind", "fog"]; //because Barcelona is paradise
    const weather_data = ["today_icon", "tomorrow_icon", "day_after_t_icon"];
    const weather_days = ["today", "tomorrow", "day after tomorrow"];
    let forecast = "";

    for (let i = 0; i < weather_data.length; i++) {
        
        let icon_name = weather_data[i]
        let text = data[icon_name].replace(/-/g, " ");
        let weather_icon;
        //use cloud icon for all overcast weather
        if (weather_ignore.includes(data[icon_name])) {
            weather_icon = "cloudy";
        } else {
            weather_icon = data[icon_name];
        }
        forecast += '<span class="weather_day" id="' + weather_days[i] + '" title="' + text + '">' + weather_days[i] + '</span><span class="weather_icon ' + weather_icon + '"> </span><span class="weather_text"> ' + text + '</span>';
    }

    let weatherinfo = document.querySelectorAll('.forecast');

    [].forEach.call(weatherinfo, function(target) {
        target.innerHTML = forecast;
    });
}

function populateDashboard(data) {
    let bat_text = "";

    if(data.charging=='no'){
      bat_text = data.charge + "%, not charging";
    }else{
      bat_text = "charging";
    }

    let footer_data = [
      ['Location', 'Barcelona'],
      ['Time', data.local_time],
      ['Battery status', bat_text],
      ['Power used', data.W],
      ['Uptime', data.uptime]
    ];

    document.getElementById('stats').innerHTML = pushData(footer_data).join("");
}

// language menu toggle
const langmenu = document.getElementById('lang-menu');
langmenu.addEventListener('click', function() {
    console.log('togglelanguages');
    document.getElementById('languages').classList.toggle("lang-expanded");
});

//mobile menu toggle
const mobilemenu = document.getElementById('m-btn');
mobilemenu.addEventListener('click', function() {
    console.log('togglemenu');
    document.getElementById('menu-list').classList.toggle("show");
});


const comments = document.querySelectorAll('.comment');
if ( comments.length > 0 ){
    //update comment count
    document.getElementById('comment-count').innerText = comments.length;
}


const dither_icons = document.querySelectorAll('.dither-toggle');
dither_icons.forEach(icon => {
	icon.addEventListener('click', function() {
	    let figure = icon.closest('.figure-controls').previousElementSibling;
	    let img = figure.querySelector('img');

	    if( figure.getAttribute('data-imgstate') == "dither"){
	    	figure.setAttribute('data-imgstate', 'undither');	    	
	    	let original = img.getAttribute('data-original');
	    	img.src = original;
	    }else{
	    	figure.setAttribute('data-imgstate', 'dither');
	    	let dither= img.getAttribute('data-dither');
	    	img.src = dither;
	    }    
	});
});
