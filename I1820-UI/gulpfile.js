/*
 * +===============================================
 * | Author:        Parham Alvani (parham.alvani@gmail.com)
 * |
 * | Creation Date: 08-11-2016
 * |
 * | File Name:     gulpfile.js
 * +===============================================
 */
var gulp = require('gulp');
var uglify = require('gulp-uglifyjs');

gulp.task('default', function() {
  gulp.src('js/*.js')
  .pipe(uglify('index.js'))
  .pipe(gulp.dest('public/'));
});
