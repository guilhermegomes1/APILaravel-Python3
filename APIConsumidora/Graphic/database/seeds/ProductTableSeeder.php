<?php

use Illuminate\Database\Seeder;
use App\Produto;
class ProductTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        factory(Produto::class, 10)->create();
    }
}
