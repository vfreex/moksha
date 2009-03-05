  <div id="${category['id']}" class="ui-sortable ${category['css_class']}">
      % for app in category['apps']:
              <span class="sort">
                % if app['label']:
            <h3>${app['label']}</h3>
            % endif

            <div id="${app['id']}" class="${app['css_class']}">
                        % if app.has_key('widget'):
                            ${app['widget'](**app['params'])}
                        % endif
                    </div>

                  % if not app.has_key('widget'):
                    <script type="text/javascript">
                          <!-- TODO: make this a JS widget -->
                          var ajaxOptions = {
                                url: moksha.csrf_rewrite_url("${app['url']}"),
                                success: function(r, s) {
                                    var $panel = $("#${app['id']}");
                                    var $stripped = moksha.filter_resources(r);
                                    $panel.html($stripped);

                                },
                                data: ${app['params']}
                          };

                          $(document).ready(function () {$.ajax(ajaxOptions)});
                    </script>
                  % endif

         </span>
      % endfor
    </div>
