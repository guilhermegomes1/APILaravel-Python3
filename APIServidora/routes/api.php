<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::namespace('Api')->name('api.')->group(function () {
    Route::prefix('filmes')->group(function(){
        Route::get('/','ProductController@index')->name('index');
        Route::get('/{id}','ProductController@show')->name('show');
        Route::post('/','ProductController@store')->name('store');
        Route::put('/{id}','ProductController@update')->name('update');
        Route::delete('/{id}', 'ProductController@delete')->name('delete');
        Route::delete('/', 'ProductController@deleteAll')->name('deleteAll');
    });
});
