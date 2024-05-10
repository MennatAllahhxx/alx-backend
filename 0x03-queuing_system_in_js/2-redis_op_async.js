import redis  from 'redis';
import { promisify } from 'util';

const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log('Redis client not connected to the server: ', err));

const get_async = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
    const value = await get_async(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

export default client;