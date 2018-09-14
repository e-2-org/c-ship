var gulp = require('gulp');
var browserSync = require('browser-sync').create();

// Static Server
gulp.task('serve', function() {
    browserSync.init({
        server: "./"
    });
});

gulp.task('default', ['serve']);