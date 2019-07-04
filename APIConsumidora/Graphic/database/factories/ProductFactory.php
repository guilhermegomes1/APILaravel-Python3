<?php

/* @var $factory \Illuminate\Database\Eloquent\Factory */

use App\Produto;
use Faker\Generator as Faker;

$factory->define(Produto::class, function (Faker $faker) {
    return [
        'name' => $faker->name,
        'price' => $faker->randomFloat(2, 0, 8),
        'description' =>$faker->text
    ];
});
