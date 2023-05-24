try {
  require.resolve('request');
  console.log('request module is installed.');
} catch (error) {
  console.log('request module is not installed.');
}

