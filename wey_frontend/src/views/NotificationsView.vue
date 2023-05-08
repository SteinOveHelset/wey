<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="notification in notifications"
                v-bind:key="notification.id"
                v-if="notifications.length"
            >
                {{ notification.body }} 

                <button class="underline" @click="readNotification(notification)">Read more</button>
            </div>

            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-else
            >
                You don't have any unread notifications!
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'notifications',

    data() {
        return {
            notifications: []
        }
    },

    mounted() {
        this.getNotifications()
    },

    methods: {
        getNotifications() {
            axios
                .get('/api/notifications/')
                .then(response => {
                    console.log(response.data)

                    this.notifications = response.data
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        },

        async readNotification(notification) {
            console.log('readNotification', notification.id)

            await axios
                .post(`/api/notifications/read/${notification.id}/`)
                .then(response => {
                    console.log(response.data)

                    if (notification.type_of_notification == 'post_like' || notification.type_of_notification == 'post_comment') {
                        this.$router.push({name: 'postview', params: {id: notification.post_id}})
                    } else {
                        this.$router.push({name: 'friends', params: {id: notification.created_for_id}})
                    }
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        }
    }
}
</script>