requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'second_index',
                js: 'secondIndex'
            }
        });
        io.start();
    }
);
