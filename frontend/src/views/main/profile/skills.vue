<template>
  <div>
    <h2>Skills Table starts here</h2>
    <table>
      <thead>
        <tr>
          <th>Sl. No</th>
          <th>Skill</th>
          <th>Remarks</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in tableData" :key="index">
          <td>{{ row.slNo }}</td>
          <td>{{ row.skill }}</td>
          <td>{{ row.remarks }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
    };
  },
  mounted() {
    // Call the API endpoint to fetch table data for the current employee
    this.fetchTableData();
  },
  methods: {
    async fetchTableData() {
      try {
        // Make an API request to fetch table data
        // Pass any necessary authentication tokens or identifiers
        const response = await axios.get('/api/skills', {
          // Include any necessary headers or tokens for authentication
          // Example: headers: { Authorization: 'Bearer your_token' }
        });

        // Assign the response data to the tableData array
        this.tableData = response.data;
      } catch (error) {
        console.error('Error fetching table datas:', error);
      }
    },
  },
};
</script>
