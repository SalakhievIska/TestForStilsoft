const requiredField = (v) => !!v || 'Обязательное поле';

const checkValueMaxLength = (value, _max) => {
  if (value) return value.length < _max;
  return true;
};

const maxLengthField = (v, _max, label) => checkValueMaxLength(v, _max) || `${label} не длинее ${_max} символов`;

const checkUrl = (url) => {
  if (url) {
    try {
      new URL(url); // eslint-disable-line no-new
      return true;
    } catch (_error) {
      return false;
    }
  } return true;
};

const urlField = (v) => checkUrl(v) || 'Ссылка не валидна';

export { requiredField, maxLengthField, urlField };
