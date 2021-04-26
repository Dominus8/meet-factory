const gulp = require('gulp');
const sass = require('gulp-sass');

function style() {
    return gulp.src('./static/css/**/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('./static/css'))
}

function watch() {
    gulp.watch('./static/css/**/*.scss', style)
}

exports.style = style;
exports.watch = watch;