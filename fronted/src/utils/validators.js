const requiredField = (v) => !!v || 'Обязательное поле';

const maxLengthField = (v, _max, label) => (v && v.length <= _max) || `${label} не длинее ${_max} символов`;

const urlField = (v) => {
  if (v) {
    try {
      const url = new URL(v);
      return !!url;
    } catch (_error) {
      return 'Ссылка не валидна';
    }
  } return true;
};

export { requiredField, maxLengthField, urlField };
