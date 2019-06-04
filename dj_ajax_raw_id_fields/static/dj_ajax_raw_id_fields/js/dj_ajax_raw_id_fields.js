// Overwrite Django's `dismissRelatedLookupPopup` to trigger a change event
// on the value change, so Salmonella can catch it and update the associated
// label.
function dismissRelatedLookupPopup(win, chosenId) {
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
        elem.value += ',' + chosenId;
    } else {
        elem.value = chosenId;
    }
    django.jQuery(elem).trigger('change');
    win.close();
}

(function($) {
    $(document).ready(function($) {

        function update_dj_ajax_raw_id_fields_label(element){

            var fake_element = $('#' + element.attr('id').replace('id_', '') + '_dj_ajax_raw_id_fields_label')
            var app = fake_element.attr("data-app"),
                model = fake_element.attr("data-model"),
                value = element.val();
            if (value.length > 0){
                var url = '';
                url = $('#site-name > a').attr('href');
                if (url.substr(url.length - 1) !== '/'){
                    url += '/';
                }
                url += 'dj_ajax_raw_id_fields/' + app + '/' + model + '/';
                $.ajax({
                    url: url,
                    data: {"id": value},
                    success: function(data){
                        fake_element.html(" " + data);
                    }
                });
                $("a[data-clear='" + element.attr('id') + "").show();
            }else{
                fake_element.html(" ");
                $("a[data-clear='" + element.attr('id') + "").hide();
            }
        }

        $(".vAjaxForeignKeyRawIdAdminField").change(function(e){
            var $this = $(this);
            update_dj_ajax_raw_id_fields_label($this, multi=false);
            e.stopPropagation();
        });

        // Clear both the input field and the labels
        $(".dj_ajax_raw_id_fields-clear-field").click(function(e){
            var element = $('#' + $(this).attr('data-clear'));
            element.val('').trigger('change');
        });

        // Open up the pop up window and set the focus in the input field
        $(".dj_ajax_raw_id_fields-related-lookup").click(function(e){
            // Actual Django javascript function
            showRelatedObjectLookupPopup(this);

            // Set the focus into the input field
            $(this).parent().find('input').focus();
            return false;
        });

        $(".vAjaxForeignKeyRawIdAdminField").each(function() {
            update_dj_ajax_raw_id_fields_label($(this));
        });

    });
})(django.jQuery);
