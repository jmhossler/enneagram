class CreateQuestions < ActiveRecord::Migration[5.0]
  def change
    create_table :questions do |t|
      t.string :test
      t.string :ans1
      t.string :ans2

      t.timestamps
    end
  end
end
