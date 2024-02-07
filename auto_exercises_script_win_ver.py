from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

#login locators and selections
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Update 07/02 sleeps added.

########################### Кастомные данные #########################################
stage = 'preview' # Значение можно менять на prod/preview/beta/bugs
login = 'test.qa.shool@gmail.com' #test.qa.edvibe@gmail.com / test.qa.shool@gmail.com
password = 'liveZvmAdjm55eB' #liveZvmAdjm55eB
choose = '2' # '1' - учитель, '2' - школа
course_name = 'Auto exercises 07/02/24' # Название для курса, при желании можно менять
section_name_in_course = 'Auto exercises test' # Название для раздела с уроком
path_to_files = os.path.abspath(os.path.join(os.path.dirname(__file__), '../exercises/materials/')) #Путь до папки с материалами
#Для запуска на win придется добавить двойные слэши к названиям картинок, увы и ах
######################################################################################

urls = {
    'prod': 'https://edvibe.com/',
    'preview': 'https://preview.edvibe.com/',
    'beta': 'https://beta.progressme.ru/',
    'bugs': 'https://bugs.progressme.ru/'
}
login_field = "//input[@name='Email']"
password_field = "//input[@name='Password']"
acc_options = {'1': '//button[.="Teacher\'s account"]',
              'teahcer_material_url': 'TeacherAccount/materials/personal',
              '2': '//button[.="Online school"]',
              'school_material_url': 'school/courses/personal'}
login_button = '.button'
exercise_modal = "//div[@class='modal-window show']"

#login actions
driver.maximize_window()
driver.get(f'{urls[stage]}Account/Login')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_field))).send_keys(login)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, password_field))).send_keys(password)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_button))).click()
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, acc_options[choose]))).click()
except:
    pass
time.sleep(3)

if choose == '1':
    driver.get(f'{urls[stage]}{acc_options["teahcer_material_url"]}')
else:
    print(f'{urls[stage]}{acc_options["school_material_url"]}')
    driver.get(f'{urls[stage]}{acc_options["school_material_url"]}')

#New course locators
new_course_button = '.create-item-btn-title'
course_avatar_button = "//div[@class='change-image-upload']/div[@class='ui-button-base gray']"
save_avatar_button = "//div[@class='row no-gutters justify-content-center pt-5']//div[@class='ui-button-base default']"
course_name_field = "[placeholder='Введите название']"
description_course_field = ".cke_textarea_inline"
language_course_menu = ".ui-select"
select_english = "//span[.='English']"
sections_enable = ".ui-toggle-switcher"
tags_menu = "//span[.='Теги']"
tags_age_filter = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите возраст')]"
adult_age_tag = "//div[@class='ui-options active multiselect']//div[@class='tag last']//div[@class='box-text option-name black']"
tags_level_filter = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите уровень')]"
intermediate_level_tag = "//div[@class='ui-options active multiselect']/div[@class='options']//div[4]//div[@class='box-text option-name black']"
tags_type_filter = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите тип')]"
main_type_tag = "//div[@class='ui-options active multiselect']//div[@class='design-flex align-center']/div[contains(.,'Общий')]"
create_course_button = ".ui-button-loading-base"

#New course actions
time.sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, new_course_button))).click()
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(f'{path_to_files}\\course_avatar.jpg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, save_avatar_button))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, course_name_field))).send_keys(course_name)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, description_course_field))).send_keys('Auto exercises test description')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, language_course_menu))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, select_english))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, sections_enable))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_menu))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_age_filter))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, adult_age_tag))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_age_filter))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_level_filter))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, intermediate_level_tag))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_level_filter))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_type_filter))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, main_type_tag))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, tags_type_filter))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, create_course_button))).click()

#Delet old section
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".box-icon[data-v-57321723]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='list-item-info-container-menu']//div[@class='box-icon icon-vertical-more']"))).click()
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='box-dropdown center default animation-up open advent']//span[.='Удалить']"))).click() #//div[@class='box-dropdown center default animation-up open advent']//span[.='Удалить']
except:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='box-dropdown center default open advent']//span[.='Удалить']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='item-button col ml-5 mr--1']/div[@class='ui-button-base default']"))).click()
time.sleep(1)

#Create custom section locators
course_xpath = f"//div[.='{course_name}']" #На всякий пускай лежит тут, дабы можно было обращаться к курсу по имени из общего списка
create_new_course_section_button = ".create-course-cont-title" #css
load_section_avatar_button = "//div[@class='change-image-upload']/div[@class='ui-button-base gray']" #xpath
save_section_avatar_button = "//div[@class='row no-gutters justify-content-center pt-5']//div[@class='ui-button-base default']"
section_name_field = "[placeholder='Введите название']" #css
section_tags_menu = "//span[.='Теги']" #xpath
section_tag_age = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите возраст')]" #xpath
section_tag_level = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите уровень')]" #xpath
section_tag_type = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите тип')]" #xpath
section_tag_skill = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите навык')]" #xpath
section_tag_time = "//div[@class='material-tag-tab']//div[@class='ui-dropdown']/div[1]/div[contains(.,'Выберите время')]" #xpath
section_field_grammar = ".material-tag-tab > div:nth-of-type(6) textarea:nth-of-type(1)" #css
section_field_vocabulary = ".material-tag-tab > div:nth-of-type(7) textarea:nth-of-type(1)" #css
section_field_functions = ".material-tag-tab > div:nth-of-type(8) textarea:nth-of-type(1)" #css
section_field_other = ".material-tag-tab > div:nth-of-type(9) textarea:nth-of-type(1)" #css
save_section_button = ".ui-button-loading-base" #css

#Create custom section actions
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, create_new_course_section_button))).click()
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(f'{path_to_files}\\section_avatar.jpg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, save_section_avatar_button))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, section_name_field))).send_keys(section_name_in_course)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, save_section_button))).click()

#Create new lesson (Тут юзаются в большинстве своем те же локаторы, что и при создании раздела, переименовывать не стала)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".list-item-info-container"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".create-lesson-cont-title"))).click()
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(f'{path_to_files}\\lesson_avatar.jpg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, save_section_avatar_button))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, section_name_field))).send_keys(section_name_in_course)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cke_textarea_inline"))).send_keys('Default auto description LolKek')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tags_menu))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_age))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, adult_age_tag))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_age))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_level))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, intermediate_level_tag))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_level))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_type))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, main_type_tag))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_type))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_skill))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='design-flex align-center']/div[contains(.,'Говорение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='design-flex align-center']/div[contains(.,'Чтение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='design-flex align-center']/div[contains(.,'Аудирование')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='tag last']//div[@class='box-text option-name black']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_skill))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, section_field_grammar))).send_keys('Auto_exercises_test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, section_field_vocabulary))).send_keys('Auto_exercises_test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, section_field_functions))).send_keys('Auto_exercises_test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, section_field_other))).send_keys('Auto_exercises_test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_time))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ui-options active multiselect']//div[@class='design-flex align-center']/div[contains(.,'60 минут')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, section_tag_time))).click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, save_section_button))).click()


#################### Exercises block ####################

#Creating exercises
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='no-exercises-plug']/div[@class='ui-button-base default']"))).click()

#P.S. Тут уже перестала выводить отдельные локаторы, т.к. в данном скрипте это просто множит строки)
#1 Picture
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Изображения')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-window show']//div[@class='exercise-block-images']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Универсальная категория] 3')
driver.find_element(By.XPATH, "//div[@class='file-input border8px']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\picture_test.jpeg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Описание']"))).send_keys('Typical picture description')
points_for_exercise = 3  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#2 GIF
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'GIF анимация')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-window show']//div[@class='exercise-block-images']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Универсальная категория] 7')
driver.find_element(By.XPATH, "//div[@class='file-input border8px hidden-input']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\gif_test.gif')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Описание']"))).send_keys('Take some rest')
points_for_exercise = 7  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#3 Video
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Видео')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-video']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория А] 10')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Например: youtube.com/watch?v=NF__BkPda8A&t']"))).send_keys('https://youtu.be/LXb3EKWsInQ?si=UdaEKEXhbVUO7-pB')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='video-box']/div[@class='content-title content']//input[@class='form-control white']"))).send_keys('Typical video description')
points_for_exercise = 10  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='scroll-container']/div[contains(.,'Категория A')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#4 Fill text with words
text_for_exercize = 'Foreign [1] languages are absolutely [2] necessary for people nowadays. More and more people [3] of different professions decide [4] to study foreign languages in order to [5] raise their professional level. Making [6] business nowadays means the ability [7] to speak at least one foreign [8] language. Among the most [9] popular foreign languages in Russia are English, [10] German, Spanish. French and Italian.'
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Заполнить пропуски словами из списка')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-block-paste-words-by-drag']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория А] 10')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-editor-input border8px control']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys(text_for_exercize)
points_for_exercise = 1  #Один балл за ответ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ответам']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='scroll-container']/div[contains(.,'Категория A')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#5 Test
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']//div[@class='block-exercise-title']/div[contains(.,'Тест')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-test']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория В] 4')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-answer-button"))).click() #Добавляем третий вариант ответа
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='add-question-button add-box border8px pointer']/div[@class='title']"))).click() #Добавляем второй вопрос
#question 1
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-test']//span[1]/div[1]//div[@class='draggable-data-sorting-wrapper exercise-block-test']/div[@class='draggable-data-sorting-item']//div[@class='input-expandable']"))).send_keys('Auto question 1')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(3) div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(1) > div:nth-of-type(1)"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(1) span:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1)"))).send_keys('Answer 1')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1)"))).send_keys('Answer 2')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(3) div:nth-of-type(3) div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1)"))).send_keys('Answer 3')
#question 2
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-test']//div[2]//div[@class='draggable-data-sorting-wrapper exercise-block-test']/div[@class='draggable-data-sorting-item']//div[@class='input-expandable']"))).send_keys('?')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(2) div:nth-of-type(3) div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(1) > div:nth-of-type(1)"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(2) span:nth-of-type(1) > div:nth-of-type(1) div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1)"))).send_keys('?')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1)"))).send_keys('!')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".exercise-test span:nth-of-type(1) > div:nth-of-type(2) div:nth-of-type(3) div:nth-of-type(3) div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1)"))).send_keys('-')
driver.execute_script("window.scrollTo(0, 0)")
points_for_exercise = 2  #Один балл за ответ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ответам']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория B')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#6 Atricle
text_for_exercize6 = 'English is the language of business correspondence, many foreign newspapers and magazines, and communication between people of different nationalities all over the world. Reading foreign literature in the original, understanding foreign films without translation, making friends with people of other nationalities may make our intellectual and cultural horizons wider.'
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Статья, сочинение или текст')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-topic']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория В] 6')
driver.find_element(By.XPATH, "//div[@class='file-input']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\for_article.jpeg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='wrapper modal crop-modal width-auto']//span[.='Создать']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Введите заголовок']"))).send_keys('Article auto test header')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='editor-input-wrapper text-title-editor']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys(text_for_exercize6)
points_for_exercise = 6  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория B')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#6.1 Composition
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Статья, сочинение или текст')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='images-type-dropdown type-dropdown']/div[@class='selected-type']/div[@class='type-option-description']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='type-options visible']/div[@class='type-box']/div[contains(.,'Поле ввода, в котором ученик может написать текст. Вы можете добавить заголовок')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-topic']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория С] 7')
driver.find_element(By.XPATH, "//div[@class='file-input']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\for_composition.jpeg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='wrapper modal crop-modal width-auto']//span[.='Создать']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Введите заголовок']"))).send_keys('Composition auto test header')
points_for_exercise = 7  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория С')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#6.2 text
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Статья, сочинение или текст')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='images-type-dropdown type-dropdown']/div[@class='selected-type']/div[@class='type-option-description']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Обычный текст.']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-topic']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория С] 8')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='editor-input-wrapper text-title-editor']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys(text_for_exercize6)
points_for_exercise = 8  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория С')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#7 Audio
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Аудиозапись')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-audio']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория D] 3')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[.='Добавить аудиофайл']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='box-dropdown top center default open advent']//button[@class='dropdown-btn']/div[contains(.,'Сгенерировать с помощью AI')]"))).click()
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-input"))).send_keys("It's auto audion test with AI")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ai-audio-generator-wrapper']/div[@class='ui-button-base default']"))).click()
time.sleep(10)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='audio-box']//input[@class='form-control white']"))).send_keys('Audio test name')
time.sleep(2)
points_for_exercise = 3  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория D')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#8 Fill text with manul words
text_for_exercize8 = 'Foreign [1/1] languages are absolutely [2/2] necessary for people nowadays. More and more people [3/3] of different professions decide [4/4] to study foreign languages in order to [5/5] raise their professional level. Making [6/6] business nowadays means the ability [7/7] to speak at least one foreign [8/8] language. Among the most [9/9] popular foreign languages in Russia are English, [10/10] German, Spanish. French and Italian.'
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[8]/div[@class='block-exercise-title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-block-paste-words-by-drag']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория D] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-editor-input border8px control']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys(text_for_exercize8)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ошибкам']"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория D')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#9 pictures - words
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Совместить слова с картинками')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='editor-input-wrapper']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категрия Е] 5')
#1 picture
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='option-word add-word']//div[@class='input-expandable']"))).send_keys('Duck')
driver.find_element(By.XPATH, "//div[@class='file-input border8px left']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\duck.jpg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='wrapper modal crop-modal width-auto']//span[.='Создать']"))).click()
#2 picture
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='option-word add-word']//div[@class='input-expandable']"))).send_keys('Frog')
driver.find_element(By.XPATH, "//div[@class='file-input border8px left']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\frog.jpg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='wrapper modal crop-modal width-auto']//span[.='Создать']"))).click()
#3 picture
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='option-word add-word']//div[@class='input-expandable']"))).send_keys('Bird')
driver.find_element(By.XPATH, "//div[@class='file-input border8px left']/input[@class='file-input-field']").send_keys(f'{path_to_files}\\bird.jpg')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='wrapper modal crop-modal width-auto']//span[.='Создать']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ошибкам']"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория E')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#10 Arrange words
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Упорядочить слова')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-make-sentence-by-words']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория Е] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='draggable-data-sorting-wrapper exercise-block-make-sentence-by-words']//div[@class='input-expandable']"))).send_keys('this/made/with/auto/test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-make-sentence-by-words']//div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-make-sentence-by-words']//span[1]/div[2]//div[@class='input-expandable']"))).send_keys('1/2/3/4/5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-make-sentence-by-words']//div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-make-sentence-by-words']/div[@class='content-block']//div[3]//div[@class='input-expandable']"))).send_keys('a/b/c/d/e/f')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ошибкам']"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория E')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#11 Choose correct answer
text_for_exercize11 = 'Foreign [1*/2/3] languages are absolutely [2*/3/4] necessary for people nowadays. More and more people [3*/4/5] of different professions decide [4*/5/6] to study foreign languages in order to [5*/6/7] raise their professional level. Making [6*/7/8] business nowadays means the ability [7*/8/9] to speak at least one foreign [8*/9/10] language. Among the most [9*/10/11] popular foreign languages in Russia are English, [10*/11/12] German, Spanish. French and Italian.'
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Выбрать правильный вариант из списка')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-block-paste-words-by-drag']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория F] 10')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-editor-input border8px control']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys(text_for_exercize11)
points_for_exercise = 1  #Один балл за ответ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ответам']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория F')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#12 True or False
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Истина или ложь')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Категория F] 3')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']//div[@class='additional-functions-title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']//div[3]//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='draggable-data-sorting-wrapper exercise-block-true-or-false']//div[@class='input-expandable']"))).send_keys('True')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='add-statement add-box border8px pointer']/div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']//span[1]/div[2]//div[@class='input-expandable']"))).send_keys('False')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='add-statement add-box border8px pointer']/div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']/div[@class='content-block']//div[3]//div[@class='option pointer']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']//div[@class='options']/div[contains(.,'Неизвестно')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-true-or-false']/div[@class='content-block']//div[3]//div[@class='input-expandable']"))).send_keys('Nope')
points_for_exercise = 1  #Один балл за ответ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ответам']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Категория F')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#13 Combine words
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[13]/div[@class='block-exercise-title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Грамматика] 3')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='add-option add-box border8px pointer']/div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[2]/div[@class='custom-input word1']/div[@class='input-expandable']"))).send_keys('1')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[2]/div[@class='custom-input word2']/div[@class='input-expandable']"))).send_keys('1')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[3]/div[@class='custom-input word1']/div[@class='input-expandable']"))).send_keys('test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[3]/div[@class='custom-input word2']/div[@class='input-expandable']"))).send_keys('test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[4]/div[@class='custom-input word1']/div[@class='input-expandable']"))).send_keys('auto')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-mapping-words']//div[4]/div[@class='custom-input word2']/div[@class='input-expandable']"))).send_keys('auto')
points_for_exercise = 1  #Один балл за ответ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ответам']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Грамматика')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#14 Make a word
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Составить слово из букв')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-build-words-from-letters']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Грамматика] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-build-words-from-letters']//div[@class='add-word add-box border8px pointer']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-build-words-from-letters']//span[1]/div[1]//div[@class='draggable-data-sorting-item']//input[@class='form-control white']"))).send_keys('test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-build-words-from-letters']//span[1]/div[1]//div[@class='draggable-data-sorting-item-footer']//input[@class='form-control white']"))).send_keys('test')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-build-words-from-letters']//span[1]/div[2]//div[@class='draggable-data-sorting-item']//input[@class='form-control white']"))).send_keys('pumpkin')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-build-words-from-letters']//span[1]/div[2]//div[@class='draggable-data-sorting-item-footer']//input[@class='form-control white']"))).send_keys('pumpkin')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ошибкам']"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Грамматика')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#15 Columns
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Расставить по колонкам')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-group-words-by-columns']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Лексика] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-group-words-by-columns']//span[1]/div[1]//div[@class='draggable-data-sorting-item']//div[@class='input-expandable']"))).send_keys('Numbers')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-group-words-by-columns']//span[1]/div[1]//div[@class='draggable-data-sorting-item-footer']//div[@class='input-expandable']"))).send_keys('1/2/3/4/5/6/7')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-group-words-by-columns']//span[1]/div[2]//div[@class='draggable-data-sorting-item']//div[@class='input-expandable']"))).send_keys('Letters')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-group-words-by-columns']//span[1]/div[2]//div[@class='draggable-data-sorting-item-footer']//div[@class='input-expandable']"))).send_keys('a/b/c/d/e/f/g')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ошибкам']"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Лексика')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#16 Text ordering
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Расставить текст по порядку')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-sentences-in-correct-order']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Лексика] 3')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-sentences-in-correct-order']//div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-sentences-in-correct-order']//span[1]/div[1]//div[@class='input-expandable']"))).send_keys('1 sentence')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-sentences-in-correct-order']//span[1]/div[2]//div[@class='input-expandable']"))).send_keys('2 sentence')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-sentences-in-correct-order']/div[@class='content-block']//div[3]//div[@class='input-expandable']"))).send_keys('3 sentence')
points_for_exercise = 1  #Один балл за ответ
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='По ответам']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Лексика')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#17 Link
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Внешняя ссылка')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-button']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Аудирование] 8')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='editor-input-wrapper editor description']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('Link description.. Look, python!')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Введите ссылку']"))).send_keys('https://overapi.com/python')
points_for_exercise = 8  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Аудирование')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#18 Note
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Заметка')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pupil-visible-box']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='editor-input-wrapper title-input']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Аудирование] 2')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-note']//div[@class='editor-input-wrapper editor']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys("It's just a note, move on")
points_for_exercise = 2  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Аудирование')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#19 Words for learn
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Набор слов для изучения')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//div[@class='add-word add-box border8px pointer']/div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//div[@class='add-word add-box border8px pointer']/div[@class='title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Чтение] 4')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//div[@class='option pointer']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//div[@class='scroll-content']/div[contains(.,'English')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//span[1]/div[1]//div[@class='custom-input word']/div[@class='input-expandable']"))).send_keys("Pumpkin")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//span[1]/div[1]//div[@class='translations-box']//div[@class='input-expandable']"))).send_keys("Тыква")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//span[1]/div[2]//div[@class='custom-input word']/div[@class='input-expandable']"))).send_keys("Game")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']//span[1]/div[2]//div[@class='translations-box']//div[@class='input-expandable']"))).send_keys("Игра")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']/div[@class='content-block']//div[3]//div[@class='custom-input word']/div[@class='input-expandable']"))).send_keys("Test")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-add-words-to-vocabulary']/div[@class='content-block']//div[3]//div[@class='translations-box']//div[@class='input-expandable']"))).send_keys("Тест")
points_for_exercise = 4  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Чтение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#20 Audio record
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Запись аудио')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-audio-recording']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Чтение] 6')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='editor-input-wrapper description-editor']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys("Just record")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='duration-box']/div[contains(.,'01:00')]"))).click()
points_for_exercise = 6  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Чтение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#21 dividing line
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Разделяющая линия')]"))).click()
points_for_exercise = 1  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Письмо')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#22 Miro
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'Доска из Miro')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-board-by-miro']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Письмо] 9')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-board-by-miro']/div[@class='content-block']/div[@class='editor-input-wrapper']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys("Tipycal miro description")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-input editor']//input[@class='form-control white']"))).send_keys("https://miro.com/app/board/uXjVNV3fhMU=/?share_link_id=570684026341")
points_for_exercise = 9  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Письмо')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#23 PDF
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='block-container']/div[@class='block-exercise pointer']/div[contains(.,'PDF из Google Drive')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-board-by-miro']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Говорение] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-board-by-miro']/div[@class='content-block']/div[@class='editor-input-wrapper']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys("Tipycal pdf description")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-input editor']//input[@class='form-control white']"))).send_keys("https://drive.google.com/file/d/1G1eRJqTKNFTOLazrjelzKi53zW6NAMyc/view?usp=sharing")
points_for_exercise = 5  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Говорение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#24 Wordwall
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[24]/div[@class='block-exercise-title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-wordwall']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Говорение] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-wordwall']/div[@class='content-block']/div[@class='editor-input-wrapper']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys("Tipycal wordwall description")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-input editor']//input[@class='form-control white']"))).send_keys('<iframe style="max-width:100%" src="https://wordwall.net/embed/0a2e6e709e834aa8958b5537267b301e?themeId=22&templateId=8&fontStackId=0" width="500" height="380" frameborder="0" allowfullscreen></iframe>')
points_for_exercise = 5  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".statistic-section-select"))).click()
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='scroll-container']/div[contains(.,'Говорение')]"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='design-flex action-buttons']/div[@class='ui-button-base default']"))).click()
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))

#25 Learning Apps
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".add_new_exercise"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[25]/div[@class='block-exercise-title']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-wordwall']//div[@class='exercise-title']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys('[Универсальная категория] 5')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='exercise-wordwall']/div[@class='content-block']/div[@class='editor-input-wrapper']//div[@class='cke_textarea_inline cke_editable cke_editable_inline cke_contents_ltr cke_show_borders']"))).send_keys("Tipycal learning app description")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='custom-input editor']//input[@class='form-control white']"))).send_keys("https://learningapps.org/2990016")
points_for_exercise = 5  # Если меняете значение тут, меняйте и в названии
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Статистика']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='toggler-with-button']//div[@class='vue-toggler']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Вручную']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(Keys.BACKSPACE)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Кол-во баллов']"))).send_keys(points_for_exercise)
time.sleep(2)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[.='Создать']"))).click()
time.sleep(2)
WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.XPATH, exercise_modal)))