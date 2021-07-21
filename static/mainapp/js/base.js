window.addEventListener("load", function() {
    (function($){
        $('#id_status').on('change', function (e) {
            var optionSelected = $("option:selected", this);
            var valueSelected = this.value;

            if (valueSelected === "Rolling"){
                $('.field-open_until').hide();
            } else {
                $('.field-open_until').show();
            }
        });
    })(django.jQuery);
});
