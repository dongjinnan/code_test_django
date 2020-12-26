$(function(){
	$('#seCity').change(function(){
		getWeather($(this).val())
	});
});

function getWeather(city){
    let param = {
        'city': city
    };

    $.ajax({
        type: 'get',
        url: '/get_weather/',
        data : param,
        success: function(result) {
			data = JSON.parse(result)
			if (data['errmsg'] != undefined && data['errmsg'] != null && data['errmsg'] != '') {
				$('#errmsg').css('display', 'block');
			} else {
				$('#city_name').text(data.city);
				$('#update_time').text(data.update_time);
				$('#weather').text(data.weather);
				$('#temperature').text(data.tem + '°C');
				$('#wind').text(data.win + '米/秒');
				$('#errmsg').css('display', 'none');
			}
        }
    });
}