<template>
    <div class="mb-6 flex items-center justify-between">
        <div class="flex items-center space-x-6">
            <img :src="comment.created_by.get_avatar" class="w-[40px] rounded-full">
            
            <p>
                <strong>
                    <RouterLink :to="{name: 'profile', params:{'id': comment.created_by.id}}">{{ comment.created_by.name }}</RouterLink>
                </strong>
            </p>
        </div>

        <p class="text-gray-600">{{ comment.created_at_formatted }} ago</p>
    </div>

    <p>{{ comment.body }}</p> 
</template>

<script>
import { RouterLink } from 'vue-router'

export default {
    props: {
        comment: Object
    },
    components: { RouterLink }
}
</script>