const requiredField = (v) => !!v || 'Обязательное поле';

const checkValueMaxLength = (value, _max) => {
  if (value) return value.length < _max;
  return true;
};

const maxLengthField = (v, _max, label) => checkValueMaxLength(v, _max) || `${label} не длинее ${_max} символов`;

const expression = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/;
const checkUrl = (url) => {
  if (url) {
    console.log(url.split(' ').length);
    if (url.split(' ').length === 1) {
      const urlRegex = new RegExp(expression);
      return urlRegex.test(url);
    } return false;
  } return true;
};

const urlField = (v) => checkUrl(v) || 'Ссылка не валидна';

export { requiredField, maxLengthField, urlField };
