const withPagination = (originalPromise) => new Promise((resolve, reject) => {
  originalPromise.then((response) => {
    resolve({
      ...response,
      paginator: {
        count: parseInt(response.headers['x-paginator-count']), // eslint-disable-line radix
        perPage: parseInt(response.headers['x-paginator-perpage']), // eslint-disable-line radix
        numPages: parseInt(response.headers['x-paginator-numpages']), // eslint-disable-line radix
      },
    });
  }).catch((error) => { reject(error); });
});

export default withPagination;
