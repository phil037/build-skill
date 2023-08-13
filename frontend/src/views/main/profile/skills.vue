<template>
  <div>
    <table v-if="userSkill.length > 0" class="table">
      <thead>
        <tr>
          <th>Skill Name</th>
          <th>Skill Value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(skill, index) in userSkill" :key="index">
          <td v-for="(value, key) in skill" :key="key">
            {{ key }}: {{ value }}
          </td>
        </tr>
      </tbody>
    </table>
    <div v-else>
      No skills available.
    </div>
  </div>
</template>


<!-- <template>
  <div class="table-container">
    <data-table :items="jsonData" :columns="tableColumns" />
  </div>
</template> -->

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
// import DataTable from '@/components/DataTable.vue';
import { Store } from 'vuex';
// import { readToken, readUserProfile } from '@/store/main/getters';
// import { readUserSkill} from '@/store/main/getters';
import { dispatchGetUserSkill } from '@/store/main/actions';

@Component
export default class UserSkill extends Vue {
  public userSkill: any = 7; // Declare userSkill as a data property

  public async created() {
    dispatchGetUserSkill(this.$store).then(skill => {
      this.userSkill = skill;
      console.log('skill returned:', skill); // Log the value
      console.log('User skill:', this.userSkill); // Log the value
    });


  }
}
// export default {
//   components: {
//     DataTable,
//   },
//   data() {
//     return {
//       jsonData: [
//         { id: 1, name: 'Alice', age: 28 },
//         { id: 2, name: 'Bob', age: 32 },
//         // Add more data here
//       ],
//       tableColumns: [
//         { key: 'id', label: 'ID' },
//         { key: 'name', label: 'Name' },
//         { key: 'age', label: 'Age' },
//         // Define more columns here
//       ],
//     };
//   },
</script>


<style>

</style>