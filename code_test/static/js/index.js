$(function(){
	$('#seCity').val($('#useCity').val());
	$('#seCity').change(function(){
		$('#chCity').val($(this).val());
		$('#chForm').submit();
	});
});