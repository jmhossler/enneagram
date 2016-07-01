class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  def question
      @question = Question.next
  end
end
