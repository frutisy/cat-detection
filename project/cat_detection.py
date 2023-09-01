from pixellib.instance import instance_segmentation


def perform_cat_detection(input_image_path: str) -> str:
    """Функция для выполнения распознавания котов на изображении."""

    # Создание экземпляра модели с использованием предобученной модели Mask R-CNN.
    segment_image = instance_segmentation()

    # Загрузка предобученной модели.
    segment_image.load_model("static/model/mask_rcnn_coco.h5")

    # Выбор классов объектов, которые будут распознаваться.
    target_class = segment_image.select_target_classes(cat=True)

    # Распознавание объектов на изображении и сохранение результата.
    result = segment_image.segmentImage(
        image_path=input_image_path,
        segment_target_classes=target_class,
        output_image_name="static/images/output_image.jpg"
    )

    # Путь к сохраненному изображению.
    output_image_path = "static/images/output_image.jpg"

    return output_image_path
