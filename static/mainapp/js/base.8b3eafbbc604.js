window.addEventListener("load", function() {
    (function($){
        $('#id_status').on('change', function (e) {
            var optionSelected = $("option:selected", this);
            var valueSelected = this.value;

            if (valueSelected === "Rolling"){
                $('#id_open_until_0').hide();
                $('#id_open_until_1').hide();
                $("label[for=id_open_until_0").hide();
            } else {
                $('#id_open_until_0').show();
                $('#id_open_until_1').show();
                $("label[for=id_open_until_0").show();
            }
        });
    })(django.jQuery);
});
